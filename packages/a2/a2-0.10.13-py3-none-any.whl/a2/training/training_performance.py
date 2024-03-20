import logging as logging_std_library

import a2.training.benchmarks
import torch
import transformers
from transformers.trainer import *  # Ugly but probably needed ... # noeq

timer = a2.training.benchmarks.import_timer()


def get_model(params):
    db_config = self.db_config_base
    if params is not None:
        db_config.update({"cls_dropout": params["cls_dropout"]})
    db_config.update({"num_labels": self.num_labels})
    model = transformers.AutoModelForSequenceClassification.from_pretrained(self.model_folder, config=db_config)
    if not base_model_trainable:
        for param in model.base_model.parameters():
            param.requires_grad = False
    if mantik:
        a2.training.tracking.initialize_mantik()
    return model


class TimerCallback(transformers.TrainerCallback):
    """
    # Example usage:
    tmr = timer.CPUGPUTimer()
    trainer = transformers.Trainer(
        # Other args...
        callbacks=[TimerCallback(tmr, gpu=True)]
    )
    trainer.train()
    tmr.print_all_time_stats()
    """

    def __init__(self, timer, gpu=False):
        super().__init__()
        self.timer = timer
        self.gpu = gpu

    def on_epoch_begin(self, args, state, control, **kwargs):
        self.timer.start(timer.TimeType.EPOCH)
        self.timer.save_all_time_stats("deep500.logs")

    def on_epoch_end(self, args, state, control, **kwargs):
        self.timer.end(timer.TimeType.EPOCH)
        self.timer.complete_all()

    def on_step_begin(self, args, state, control, **kwargs):
        logging_std_library.info(
            f"Epoch {int(state.epoch)}: Start iteration step {state.global_step}/{state.max_steps} of training..."
        )
        self.timer.start(timer.TimeType.BATCH)

    def on_step_end(self, args, state, control, **kwargs):
        self.timer.end(timer.TimeType.BATCH)
        if state.global_step % 10 == 0:
            self.timer.complete_all()


class TimeLoaderWrapper:
    """Wrapper around a DataLoader (*not* a Dataset!) for I/O timing."""

    def __init__(self, loader, timer):
        self.loader = loader
        self.tmr = timer

    @staticmethod
    def time_loader(loader, tmr):
        if len(loader) > 0:
            tmr.start(timer.TimeType.IO)
        for i, data in enumerate(loader):
            tmr.end(timer.TimeType.IO)
            if i % 10 == 0:
                tmr.complete_all()
            yield data
            if i != len(loader) - 1:
                tmr.start(timer.TimeType.IO)

    def __iter__(self):
        return TimeLoaderWrapper.time_loader(self.loader, self.tmr)

    def __len__(self):
        return len(self.loader)

    def reset(self):
        if hasattr(self.loader, "reset"):
            self.loader.reset()


class TrainerWithTimer(Trainer):
    """
    Custom Trainer subclass to support finer-grained timing.
    Should also use the callback above.
    Adapted from original:
    # https://github.com/huggingface/transformers/blob/v4.25.1/src/transformers/trainer.py
    """

    def __init__(self, *args, **kwargs):
        print(f'{kwargs["callbacks"]=}')
        self.timer_callback = kwargs["callbacks"][0]
        self.tmr = self.timer_callback.timer
        self.tmr_gpu = self.timer_callback.gpu
        super().__init__(*args, **kwargs)

    def training_step(self, model, inputs):
        model.train()
        inputs = self._prepare_inputs(inputs)

        if self.tmr:
            self.tmr.start(timer.TimeType.FORWARD)
        with self.compute_loss_context_manager():
            loss = self.compute_loss(model, inputs)

        if self.args.n_gpu > 1:
            loss = loss.mean()  # mean() to average on multi-gpu parallel training

        if self.args.gradient_accumulation_steps > 1 and not self.deepspeed:
            # deepspeed handles loss scaling by gradient_accumulation_steps in its `backward`
            loss = loss / self.args.gradient_accumulation_steps
        if self.tmr:
            self.tmr.end(timer.TimeType.FORWARD)
            self.tmr.start(timer.TimeType.BACKWARD)
        print(f"{self.do_grad_scaling=}")
        print(f"{self.use_apex=}")
        print(f"{self.deepspeed=}")
        if self.do_grad_scaling:
            self.scaler.scale(loss).backward()
        elif self.use_apex:
            with amp.scale_loss(loss, self.optimizer) as scaled_loss:
                scaled_loss.backward()
        elif self.deepspeed:
            # loss gets scaled under gradient_accumulation_steps in deepspeed
            loss = self.deepspeed.backward(loss)
        else:
            loss.backward()

        if self.tmr:
            self.tmr.end(timer.TimeType.BACKWARD)

        return loss.detach()

    def get_train_dataloader(self):
        if self.train_dataset is None:
            raise ValueError("Trainer: training requires a train_dataset.")

        train_dataset = self.train_dataset
        data_collator = self.data_collator
        if is_datasets_available() and isinstance(train_dataset, datasets.Dataset):
            train_dataset = self._remove_unused_columns(train_dataset, description="training")
        else:
            data_collator = self._get_collator_with_removed_columns(data_collator, description="training")

        if isinstance(train_dataset, torch.utils.data.IterableDataset):
            if self.args.world_size > 1:
                train_dataset = IterableDatasetShard(
                    train_dataset,
                    batch_size=self._train_batch_size,
                    drop_last=self.args.dataloader_drop_last,
                    num_processes=self.args.world_size,
                    process_index=self.args.process_index,
                )

            dl = DataLoader(
                train_dataset,
                batch_size=self.args.per_device_train_batch_size,
                collate_fn=data_collator,
                num_workers=self.args.dataloader_num_workers,
                pin_memory=self.args.dataloader_pin_memory,
            )
        else:
            train_sampler = self._get_train_sampler()

            dl = DataLoader(
                train_dataset,
                batch_size=self._train_batch_size,
                sampler=train_sampler,
                collate_fn=data_collator,
                drop_last=self.args.dataloader_drop_last,
                num_workers=self.args.dataloader_num_workers,
                pin_memory=self.args.dataloader_pin_memory,
                worker_init_fn=seed_worker,
            )

        if self.tmr:
            return TimeLoaderWrapper(dl, self.tmr)
        return dl

    def save_model(self, output_dir: Optional[str] = None, _internal_call: bool = False):
        self.tmr.start(timer.TimeType.SAVING_MODEL)
        super().save_model(output_dir=output_dir, _internal_call=_internal_call)
        self.tmr.end(timer.TimeType.SAVING_MODEL)
