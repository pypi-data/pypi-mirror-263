from pathlib import Path
from typing import Optional, Union

import torch
from torch.utils.data import DataLoader, DistributedSampler
from torchinfo import summary
from tqdm import tqdm

from ...src.losses.dino_loss import DINOLoss
from ...src.models.dino.head import DINOHead
from ...src.models.dino.multi_crop_wrapper import MultiCropWrapper
from ...src.models.encoders.utils import get_encoder_class
from ...src.models.utils import (
    ModelType,
    cancel_gradients_last_layer,
    cosine_scheduler,
    ema_update_teacher,
    get_params_groups,
)
from ...src.optimizers.utils import get_optimizer_type
from ...src.pkg.wrappers import ViTWrapper, Wrapper
from ...src.trainers.base_trainer import Trainer
from ...src.utils.metrics import (
    calculate_embedding_entropy,
    calculate_student_teacher_acc,
)
from ...src.utils.utils import (
    clip_gradients,
    get_world_size,
    restart_from_checkpoint,
    save_checkpoint,
    set_requires_grad,
)


class DINOTrainer(Trainer):
    def __init__(
        self,
        train_dataset: DataLoader,
        config: dict,
        val_dataset: Optional[DataLoader] = None,
        config_path: Optional[Union[str, Path]] = None,
        additional_run_info: str = "",
        additional_arch_info: str = "",
        print_model_summary: bool = False,
        wandb_logging: bool = True,
        wandb_project_name="SSL",
    ):
        super().__init__(
            train_dataset=train_dataset,
            val_dataset=val_dataset,
            config=config,
            config_path=config_path,
            arch_name=f"DINO{additional_arch_info}",
            additional_run_info=additional_run_info,
            wandb_logging=wandb_logging,
            wandb_project_name=wandb_project_name,
        )
        self.print_model_summary = print_model_summary
        self.n_g_crops = self.config["dataset"]["augmentations"]["global_crops_number"]
        self.n_l_crops = self.config["dataset"]["augmentations"]["local_crops_number"]
        # get the architecture for student and teacher
        encoder_cls, model_type = get_encoder_class(self.config["model"]["base_model"])
        if model_type is ModelType.VIT:
            self.student = encoder_cls(**self.config["model"].get("student", {}))
            self.teacher = encoder_cls(**self.config["model"].get("teacher", {}))
            self.embed_dim = self.student.embed_dim
        elif model_type is ModelType.CNN:
            self.student = encoder_cls(
                weights=self.config["model"]["student"]["weights"]
            )
            self.teacher = encoder_cls(
                weights=self.config["model"]["teacher"]["weights"]
            )
            self.embed_dim = self.student.fc.weight.shape[1]
        else:
            raise ValueError(f"Unknown model type: {model_type}")
        # define the loss function
        self.loss = DINOLoss(
            out_dim=self.config["model"]["out_dim"],
            n_epochs=self.config["epochs"],
            n_crops=self.n_g_crops + self.n_l_crops,
            n_g_crops=self.n_g_crops,
            **self.config["loss"],
        )
        self.loss = self.loss.to(self.device)
        if wandb_logging:
            import wandb

    def fit(self) -> torch.nn.Module:
        # build models (student and teacher)
        # multi-crop wrapper handles forward with inputs of diff. resolutions
        self.student = MultiCropWrapper(
            backbone=self.student,
            head=DINOHead(
                self.embed_dim,
                self.config["model"]["out_dim"],
                use_bn=self.config["model"]["use_bn_in_head"],
                norm_last_layer=self.config["model"]["norm_last_layer"],
            ),
            apply_l2_norm=self.config["apply_l2_norm"],
        )
        self.student = self.student.to(self.device)
        self.student = self.distribute_model(self.student)

        self.teacher = MultiCropWrapper(
            backbone=self.teacher,
            head=DINOHead(
                self.embed_dim,
                self.config["model"]["out_dim"],
                use_bn=self.config["model"]["use_bn_in_head"],
            ),
            apply_l2_norm=self.config["apply_l2_norm"],
        )
        self.teacher = self.teacher.to(self.device)
        self.teacher = self.distribute_model(self.teacher)

        # teacher and student start with the same weights
        self.teacher.load_state_dict(self.student.state_dict())
        # no backpropagation through the teacher, so no need for gradients
        set_requires_grad(self.teacher, False)
        print(
            f"Student and Teacher are built: they are both "
            f"{self.config['model']['base_model']} network."
        )

        if self.print_model_summary:
            print("*" * 20 + " Student " + "*" * 20)
            summary(self.student, input_size=(self.config["batch_size"], 3, 224, 224))
            print("*" * 20 + " Teacher " + "*" * 20)
            summary(self.teacher, input_size=(self.config["batch_size"], 3, 224, 224))

        # create optimizer
        params_groups = get_params_groups(self.student)
        optimizer_cls = get_optimizer_type(self.config["optim"])
        optimizer = optimizer_cls(params_groups)

        # create schedulers
        lr_schedule = cosine_scheduler(
            # linear scaling rule
            self.config["lr"] * (self.config["batch_size"] * get_world_size()) / 256.0,
            eval(self.config["min_lr"]),
            self.config["epochs"],
            len(self.train_dataset),
            warmup_epochs=min(self.config["warmup_epochs"], self.config["epochs"]),
        )
        wd_schedule = cosine_scheduler(
            self.config["weight_decay"],
            self.config["weight_decay_end"],
            self.config["epochs"],
            len(self.train_dataset),
        )
        # momentum parameter is increased to 1. during training with a cosine schedule
        momentum_schedule = cosine_scheduler(
            self.config["momentum_teacher"],
            1,
            self.config["epochs"],
            len(self.train_dataset),
        )

        # load the model from checkpoint if provided
        to_restore = {"epoch": 0, "config": self.config}
        if (self.get_ckp_path / "model_best.pth").exists():
            restart_from_checkpoint(
                self.get_ckp_path / "model_best.pth",
                run_variables=to_restore,
                student=self.student,
                teacher=self.teacher,
                optimizer=optimizer,
                loss=self.loss,
                debug=False,
            )
        self.start_epoch = to_restore["epoch"] + 1
        self.config = to_restore["config"]

        # save the config.yaml file
        self._save_config_file(self.run_dir / "checkpoints")

        # log embedding before training
        self._log_embeddings(
            model=self.student,
            log_self_attention=self.config.get("visualize_attention", False),
            log_dict={
                "counters/epoch": 0,
                "counters/train_step": 0,
            },
        )

        # perform the SSL pre-training
        if self.config.get("ssl_pre_training", True):
            self._model_training(
                optimizer=optimizer,
                lr_schedule=lr_schedule,
                wd_schedule=wd_schedule,
                momentum_schedule=momentum_schedule,
            )

        if self.multi_gpu:
            backbone = self.student.module.backbone
        else:
            backbone = self.student.backbone
        if self.model_type is ModelType.VIT:
            model = ViTWrapper(backbone)
        else:
            model = Wrapper(model=backbone)
        return model

    def _model_training(self, optimizer, lr_schedule, wd_schedule, momentum_schedule):
        n_iter = 0
        progress_bar = tqdm(range(self.start_epoch, self.config["epochs"] + 1))
        for epoch in progress_bar:
            if type(self.train_dataset.sampler) is DistributedSampler:
                self.train_dataset.sampler.set_epoch(epoch - 1)
            self.student.train()
            for images, *_ in self.train_dataset:
                # update weight decay and learning rate according to their schedule
                self.update_optim_from_schedulers(
                    optimizer=optimizer,
                    lr_schedule=lr_schedule,
                    wd_schedule=wd_schedule,
                    n_iter=n_iter,
                )

                # move images to device
                images = [im.to(self.device, non_blocking=True) for im in images]

                # zero the parameter gradients
                optimizer.zero_grad()

                # --- forward pass ---
                # only the 2 global views pass through the teacher
                teacher_output = self.teacher(images[: self.n_g_crops])
                student_output = self.student(images)
                loss = self.loss(student_output, teacher_output, epoch - 1)

                # check if loss is not infinite
                self.check_loss_nan(loss.detach())

                # student update
                loss.backward()
                if self.config["clip_grad"]:
                    _ = clip_gradients(self.student, self.config["clip_grad"])
                cancel_gradients_last_layer(
                    epoch - 1,
                    self.student,
                    self.config["optimizer"]["freeze_last_layer"],
                )
                optimizer.step()

                # EMA update for the teacher
                ema_update_teacher(
                    student=self.student,
                    teacher=self.teacher,
                    momentum_schedule=momentum_schedule,
                    n_iter=n_iter,
                )

                # calculate the entropy of the emb. space
                emb_glob = self._get_embedding(
                    model=self.student,
                    images=torch.concat(images[: self.n_g_crops]),
                ).cpu()
                emb_loc = self._get_embedding(
                    model=self.student,
                    images=torch.concat(images[self.n_g_crops :]),
                ).cpu()
                entropy = calculate_embedding_entropy(
                    embeddings=torch.concat([emb_glob, emb_loc])
                )
                ent_avg, ent_min, ent_max, ent_std, ent_med = entropy

                # log metrics
                acc = calculate_student_teacher_acc(
                    teacher_output.cpu(),
                    student_output[: self.n_g_crops].cpu(),
                    self.n_g_crops,
                )
                progress_bar.set_description(
                    f"Epoch: {epoch}, "
                    f"Train loss: {loss:.6f}, "
                    f"Train stud/teach acc: {acc:.4f}"
                )
                lr = optimizer.param_groups[0]["lr"]
                wd = optimizer.param_groups[0]["weight_decay"]
                log_dict = {
                    "train_loss": loss,
                    "train_stud_teach_acc": acc,
                    "lr": lr,
                    "weight_decay": wd,
                    "entropy/train_ent_avg": ent_avg,
                    "entropy/train_ent_min": ent_min,
                    "entropy/train_ent_max": ent_max,
                    "entropy/train_ent_std": ent_std,
                    "entropy/train_ent_med": ent_med,
                    "counters/epoch": epoch,
                    "counters/train_step": n_iter,
                }
                if self.wandb_logging:
                    wandb.log(log_dict)
                n_iter += 1

            # log the embeddings if wanted (included online evaluation)
            if epoch % self.config.get("embed_vis_every_n_epochs", -1) == 0:
                self._log_embeddings(
                    model=self.student,
                    log_self_attention=self.config.get("visualize_attention", False),
                    log_dict={
                        "counters/epoch": epoch,
                        "counters/train_step": n_iter,
                    },
                )

            # save the model
            if (
                epoch % self.config.get("save_every_n_epochs", self.config["epochs"])
                == 0
            ):
                if self.multi_gpu:
                    student = self.student.module.state_dict()
                    teacher = self.teacher.module.state_dict()
                else:
                    student = self.student.state_dict()
                    teacher = self.teacher.state_dict()
                save_dict = {
                    "arch": type(self.student).__name__,
                    "epoch": epoch,
                    "student": student,
                    "teacher": teacher,
                    "optimizer": optimizer.state_dict(),
                    "config": self.config,
                    "loss": self.loss.state_dict(),
                }
                save_checkpoint(
                    run_dir=self.run_dir,
                    save_dict=save_dict,
                    epoch=epoch,
                    save_best=True,
                )
