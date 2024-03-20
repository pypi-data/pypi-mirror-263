import logging as logging_std_library

import a2.training.benchmarks
import a2.utils.utils
import transformers
from transformers.trainer import *  # Ugly but probably needed ... # noeq

timer = a2.training.benchmarks.import_timer()

torch = a2.utils.utils._import_torch(__file__)


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

    def training_step(self, model: nn.Module, inputs: Dict[str, Union[torch.Tensor, Any]]) -> torch.Tensor:
        """
        Perform a training step on a batch of inputs.

        Subclass and override to inject custom behavior.

        Args:
            model (`nn.Module`):
                The model to train.
            inputs (`Dict[str, Union[torch.Tensor, Any]]`):
                The inputs and targets of the model.

                The dictionary will be unpacked before being fed to the model. Most models expect the targets under the
                argument `labels`. Check your model's documentation for all accepted arguments.

        Return:
            `torch.Tensor`: The tensor with training loss on this batch.
        """
        model.train()
        inputs = self._prepare_inputs(inputs)

        if is_sagemaker_mp_enabled():
            loss_mb = smp_forward_backward(model, inputs, self.args.gradient_accumulation_steps)
            return loss_mb.reduce_mean().detach().to(self.args.device)
        if self.tmr:
            self.tmr.start(timer.TimeType.FORWARD)

        with self.compute_loss_context_manager():
            loss = self.compute_loss(model, inputs)

        if self.args.n_gpu > 1:
            loss = loss.mean()  # mean() to average on multi-gpu parallel training
        if self.tmr:
            self.tmr.end(timer.TimeType.FORWARD)
            self.tmr.start(timer.TimeType.BACKWARD)

        if self.use_apex:
            with amp.scale_loss(loss, self.optimizer) as scaled_loss:
                scaled_loss.backward()
        else:
            self.accelerator.backward(loss)
        if self.tmr:
            self.tmr.end(timer.TimeType.BACKWARD)

        return loss.detach() / self.args.gradient_accumulation_steps

    def get_train_dataloader(self) -> DataLoader:
        dl = super().get_train_dataloader()
        if self.tmr:
            return TimeLoaderWrapper(dl, self.tmr)
        return dl

    def save_model(self, output_dir: Optional[str] = None, _internal_call: bool = False):
        # self.tmr.start(timer.TimeType.OTHER)
        super().save_model(output_dir=output_dir, _internal_call=_internal_call)
        # self.tmr.end(timer.TimeType.OTHER)
