# -*- coding: utf-8 -*-
import collections
import importlib
import os
import sys
from datetime import datetime
from string import Template
from types import SimpleNamespace

import hao
import torch
import torchinfo
from hao.exits import OnExit
from hao.namespaces import attr, from_args
from peft import PeftType, TaskType, get_peft_config, get_peft_model_state_dict, set_peft_model_state_dict
from torch.nn.parallel import DistributedDataParallel
from torch.utils.data.dataloader import DataLoader

from tailors import move_to_device, off_device, set_seed
from tailors.models import Tailors
from tailors.trainer import callbacks, model_size, optimizers, pefts, schedulers
from tailors.trainer.data import DatasetConf, TailorDataset
from tailors.trainer.exceptions import StopTailorsTrainer
from tailors.utils import tweezer
from tailors.utils.progresses import progressive

LOGGER = hao.logs.get_logger('trainer')


@from_args
class TaskConf:
    task: str = attr(str, help='using predefined values in `tasks.{task}` in tailors.yml')


@from_args
class TrainConf:
    """Hyperparams"""
    model: str = attr(str, required=True)
    dataset: str = attr(str, required=True)
    seed = attr(int, default=1000)
    max_epochs: int = attr(int, default=50)
    lr: float = attr(float, required=True)
    optimizer = attr(str, choices=tuple(optimizers.OPTIMIZERS), default=list(optimizers.OPTIMIZERS)[0])
    weight_decay: float = attr(float, default=1e-2)
    scheduler: str = attr(str, choices=tuple(schedulers.SCHEDULERS), default=list(schedulers.SCHEDULERS)[0])
    clip_norm: float = attr(float, default=0.1)
    amp: bool = attr(bool, default=False)
    accumulation: int = attr(int, default=1)
    peft: str = attr(str, choices=tuple(t.value.lower() for t in PeftType), default=None)
    peft_task_type: str = attr(str, choices=tuple(t.value.lower() for t in TaskType))


@from_args
class TrainerConf:
    """Non-hyperparams"""
    exp: str = attr(str, required=True)
    ts: str = attr(str, help='do not set it manully', default=lambda: datetime.now().strftime('%y%m%d-%H%M'))
    gpus: str = attr(str, help='gpu indices separated by comma, no spaces')
    log_model_summary: bool = attr(bool, default=True)
    log_model_depth: int = attr(int, default=3)
    resume_from: str = attr(str)
    early_stop_patience: int = attr(int, default=5)
    measure: str = attr(str, help='the main metric name to measure the performance, such as "f1", "acc"..., will guess one if not specified')
    checkpoint_name: str = attr(str, default='{model}-{dataset}-{exp}-{ts}-epoch={epoch}-val_loss={loss_val}-${measure}={${measure}}.ckpt')
    save_top_n: int = attr(int, default=1)
    save_last: bool = attr(bool, default=False)


class TrainerState:
    def __init__(self, ts: str | None = None) -> None:
        self.ts = ts or datetime.now().strftime('%y%m%d-%H%M')
        self.bz = 0
        self.steps_per_epoch = {}
        self.step = 0
        self.epoch = -1
        self.progress = {}
        self.took = None
        self.batch_id = -1
        self.val_losses = []
        self.score = {}
        self.metrics = {}
        self.reports = {}
        self._ckpts = SimpleNamespace(top_n=[], last=None, should_save=False, new_path=None)
        self._resume_state_dict = None

    def set_metric(self, key, value):
        self.metrics[key] = value
        if key == 'loss/val':
            self.val_losses.append(value)

    def set_metrics(self, metrics: dict):
        for k, v in metrics.items():
            if 'report' in k.lower():
                self.reports[k] = v
            else:
                self.set_metric(k, v)

    def state_dict(self):
        return {k: v for k, v in vars(self).items() if not k.startswith('_')}

    def load_state_dict(self, state_dict):
        for k, v in state_dict.items():
            setattr(self, k, v)


class Trainer(OnExit):
    def __init__(self, trainer_conf: TrainerConf | None = None, train_conf: TrainConf | None = None) -> None:
        super().__init__()
        self.task_conf = TaskConf()
        self.trainer_conf = trainer_conf or TrainerConf()
        self.train_conf = train_conf or TrainConf()
        LOGGER.info(self.trainer_conf)
        LOGGER.info(self.train_conf)
        self.device, self.rank, self.world_size = self.check_devices()
        self.state = TrainerState(self.trainer_conf.ts)
        self.exp_dir = f"data/exps/{self.train_conf.model}/{self.train_conf.dataset}/{self.trainer_conf.exp}-{self.state.ts}"
        self.prepare_resume_from()

        set_seed(self.train_conf.seed)
        self.model, self.model_conf = self.get_model()
        self.dataloaders, self.state.steps_per_epoch, self.dataset_conf = self.get_dataloaders()

        self.scaler = self.get_scaler()
        self.optimizer, self.optimizer_conf = self.get_optimizer()
        self.scheduler, self.scheduler_conf = self.get_scheduler()
        self.callback_handler = callbacks.CallbackHandler(self)

        self.validate()

        self.process_resume_from()
        self.log_model_summary()

    def check_devices(self):
        rank = 0
        if self.trainer_conf.gpus:
            gpus = [gpu for gpu in self.trainer_conf.gpus.split(',') if gpu and gpu.isdigit() and 0 <= int(gpu)]
            cuda_visible_devices = ','.join(gpus)
            os.environ['CUDA_VISIBLE_DEVICES'] = cuda_visible_devices
            LOGGER.info(f"CUDA_VISIBLE_DEVICES={cuda_visible_devices}")

            is_cuda_available, n_devices = torch.cuda.is_available(), torch.cuda.device_count()
            if is_cuda_available and n_devices > 0:
                device = torch.device(f"cuda:{rank}")
                LOGGER.info(f"[device] {device}, cuda available: {is_cuda_available}, device count: {n_devices}")
                return device, rank, n_devices
        else:
            is_cuda_available, n_devices = torch.cuda.is_available(), torch.cuda.device_count()

        device = torch.device('cpu')
        LOGGER.info(f"[device] {device}, cuda available: {is_cuda_available}, device count: {n_devices}")
        return device, rank, n_devices

    def prepare_resume_from(self):
        checkpoint_path = hao.paths.get(self.trainer_conf.resume_from)
        if checkpoint_path is None or not os.path.isfile(checkpoint_path):
            return
        LOGGER.info(f"[resume from] {checkpoint_path}")
        self.state._resume_state_dict = torch.load(checkpoint_path)

    def validate(self):
        pass

    def process_resume_from(self):
        if self.state._resume_state_dict is None:
            return
        for key, attri in (
            ('state', 'state'),
            ('state_dict', 'model'),
            ('scaler_state_dict', 'scaler'),
            ('optimizer_state_dict', 'optimizer'),
            ('scheduler_state_dict', 'scheduler'),
        ):
            if (m := getattr(self, attri, None)) is None or (state_dict := self.state._resume_state_dict.get(key)) is None:
                continue
            m.load_state_dict(state_dict)

        model_state_dict = self.state._resume_state_dict.get('state_dict')
        if (peft_config := self.state._resume_state_dict.get('peft_config')) is None:
            self.model.load_state_dict(model_state_dict)
        else:
            self.model.peft_config = get_peft_config(peft_config)
            set_peft_model_state_dict(self.model, model_state_dict)
        self.state._resume_state_dict = None

    def get_model(self) -> Tailors:
        model_fqn = self.train_conf.model
        module_name, _, model_class_name = model_fqn.rpartition('.')
        module = importlib.import_module(module_name)
        model_class = getattr(module, model_class_name)

        if self.state._resume_state_dict is not None:
            model_conf = self.state._resume_state_dict.get('model_conf')
        else:
            model_conf_class = getattr(module, f"{model_class_name}Conf")
            meta = hao.config.get(f"datasets.{self.train_conf.dataset}", config='tailors.yml').get('meta')
            model_conf = model_conf_class(meta=meta)
        LOGGER.info(model_conf)
        model = model_class(model_conf)
        model = pefts.peftify(model, self.train_conf.peft, self.train_conf.peft_task_type)
        model.use_device(self.device)

        if self.world_size > 1:
            model = DistributedDataParallel(model, device_ids=[self.rank], output_device=self.rank)
        return model, model_conf

    def get_dataloaders(self):
        datasets = hao.config.get(f"datasets.{self.train_conf.dataset}", config='tailors.yml').get('dataset')
        dataset_conf = DatasetConf()
        LOGGER.info(dataset_conf)
        self.state.bz = dataset_conf.bz
        dataloaders = {
            split: TailorDataset(self.model.io, self.train_conf.dataset, split, files, dataset_conf).dataloader()
            for split, files in datasets.items()
        }
        steps_per_epochs = {split: len(dataloader) for split, dataloader in dataloaders.items()}
        return dataloaders, steps_per_epochs, dataset_conf

    def get_scaler(self):
        return torch.cuda.amp.GradScaler() if self.train_conf.amp else None

    def get_optimizer(self):
        def get_bucket(name):
            for key in rates:
                if name.startswith(key):
                    return key
            return 'default'

        rates = {name: f.apply(self.train_conf.lr) for name, f in self.model.lr_factors().items()}

        no_decay = ['bias', 'gamma', 'beta', 'LayerNorm.weight', 'LayerNorm.bias']
        no_decay_suffix = '_no_decay'
        groups_default, groups_named, group_meta = collections.defaultdict(list), collections.defaultdict(list), {}
        for n, p in self.model.named_parameters():
            if len(p) == 0:
                continue
            bucket = get_bucket(n)
            is_no_decay = any(nd in n for nd in no_decay)
            groups = groups_default if bucket == 'default' else groups_named
            key = f"{bucket}{no_decay_suffix}" if is_no_decay else bucket
            groups[key].append(p)
            if key not in group_meta:
                weight_decay = 0 if is_no_decay else self.train_conf.weight_decay
                lr = rates.get(bucket, self.train_conf.lr)
                group_meta[key] = {'weight_decay': weight_decay, 'lr': lr, 'name': key}

        grouped_parameters = []
        for key, params in groups_default.items():
            grouped_parameters.append({'params': params, **group_meta.get(key)})
        for key, params in groups_named.items():
            grouped_parameters.append({'params': params, **group_meta.get(key)})
        return optimizers.get(self.train_conf.optimizer, grouped_parameters)

    def get_scheduler(self):
        return schedulers.get(
            self.train_conf.scheduler,
            self.optimizer,
            max_epochs=self.train_conf.max_epochs,
            steps_per_epoch=self.state.steps_per_epoch.get('train'),
        )

    def log_model_summary(self):
        if self.trainer_conf.log_model_summary:
            summary = torchinfo.summary(
                self.model,
                col_names=('num_params', 'trainable'),
                mode='train',
                row_settings=('ascii_only',),
                depth=self.trainer_conf.log_model_depth,
                verbose=0,
            )
            LOGGER.info(f"[summary] {self.train_conf.model}\n{summary}")
            LOGGER.info(f"estimated size: {model_size(self.model)}")

    def get_lr(self):
        if hasattr(self.scheduler, 'get_lr'):
            return self.scheduler.get_lr()
        return self.get_lrs()[0]

    def get_lrs(self):
        return [group["lr"] for group in self.optimizer.param_groups]

    def fit(self):
        LOGGER.info('[fit] start')
        sw = hao.stopwatch.Stopwatch()
        self.prepare_fit()
        self.callback_handler.on_fit_start()
        try:
            dataloader_train, dataloader_val = self.dataloaders.get('train'), self.dataloaders.get('val')
            for epoch in range(self.state.epoch + 1, self.train_conf.max_epochs):
                LOGGER.info(f"({self.task_conf.task}) [epoch {epoch}] start")
                self.state.epoch = epoch
                self.callback_handler.on_epoch_start()
                self.train_epoch(epoch, dataloader_train)
                self.val_epoch(epoch, dataloader_val)
                if self.scheduler_conf.interval == 'epoch':
                    self.lr_scheduler_step()
                self.log_metrics()

                self.state.took = sw.took(millis=False)
                self.callback_handler.on_epoch_end()
                self.save_if_should()
                LOGGER.info(f"({self.task_conf.task}) [epoch {epoch}] end, took {sw.lap()}")
        except StopTailorsTrainer:
            pass
        finally:
            try:
                if self.trainer_conf.save_last:
                    self.state._ckpts.last = self.save(is_last=True)
            except Exception as e:
                LOGGER.exception(e)
            self.callback_handler.on_fit_end()
            self.save_model()
            LOGGER.info(f"[fit] end, took: {sw.took()}")

    def on_exit(self):
        sys.exit(0)

    def prepare_fit(self):
        set_seed(self.train_conf.seed)

        # ignore tokenizer fork warning
        os.environ['TOKENIZERS_PARALLELISM'] = 'false'

        # RuntimeError: unable to open shared memory object
        torch.multiprocessing.set_sharing_strategy('file_system')

    def train_epoch(self, epoch: int, dataloader: DataLoader):
        self.model.train()
        self.state.progress = {'stage': 'train', 'epoch': epoch}
        self.callback_handler.on_train_epoch_start(epoch)
        losses = []
        acmu = max(1, self.train_conf.accumulation)
        with progressive(dataloader, desc=f"({self.task_conf.task}) [epoch {epoch}] train", ascii=' ━', colour='blue') as batches:
            for batch_id, batch in enumerate(batches):
                self.state.batch_id = batch_id
                self.state.step += acmu
                self.callback_handler.on_train_batch_start()

                batch = move_to_device(batch, self.model.device)
                is_optimizer_step = acmu == 1 or self.state.step % acmu == 0

                if self.scaler:
                    with torch.cuda.amp.autocast(True):
                        batch_out = self.model.train_step(batch.features, batch.target)

                    loss = tweezer.get(batch_out, 'loss')
                    if loss is None:
                        raise RuntimeError('train_step should return loss')
                    loss = loss / acmu
                    self.scaler.scale(loss).backward()
                    loss = loss.item()
                    losses.append(loss)
                    if self.train_conf.clip_norm > 0:
                        self.scaler.unscale_(self.optimizer)
                        torch.nn.utils.clip_grad_norm_(self.model.parameters(), self.train_conf.clip_norm)
                    if is_optimizer_step:
                        self.scaler.step(self.optimizer)
                        self.scaler.update()
                        self.optimizer.zero_grad(set_to_none=True)
                        batches.set_postfix({'loss': f"{loss:.4f}", 'ts': self.state.ts})

                else:
                    batch_out = self.model.train_step(batch.features, batch.target)
                    loss = tweezer.get(batch_out, 'loss')
                    if loss is None:
                        raise RuntimeError('train_step should return loss')
                    loss = loss / acmu
                    loss.backward()
                    loss = loss.item()
                    losses.append(loss)

                    if self.train_conf.clip_norm > 0:
                        torch.nn.utils.clip_grad_norm_(self.model.parameters(), self.train_conf.clip_norm)
                    if is_optimizer_step:
                        self.optimizer.step()
                        self.optimizer.zero_grad(set_to_none=True)
                        batches.set_postfix({'loss': f"{loss:.4f}", 'ts': self.state.ts})

                self.update_progress_state(batches)
                self.callback_handler.on_train_batch_end(epoch, batch, batch_out)
                if self.scheduler_conf.interval == 'step':
                    self.lr_scheduler_step()

        self.state.set_metric('loss/train', sum(losses) / len(losses))
        self.callback_handler.on_train_epoch_end(epoch)

    def val_epoch(self, epoch: int, dataloader: DataLoader):
        self.model.eval()
        self.state.progress = {'stage': 'val', 'epoch': epoch}
        self.callback_handler.on_val_epoch_start()
        losses, batch_outs, targets = [], [], []
        with progressive(dataloader, desc=f"({self.task_conf.task}) [epoch {epoch}] val  ", ascii=' ━', colour='green') as batches, torch.no_grad():
            for batch_id, batch in enumerate(batches):
                self.state.batch_id = batch_id
                self.callback_handler.on_val_batch_start()

                batch = move_to_device(batch, self.model.device)
                batch_out = self.model.val_step(batch.features, batch.target)
                batch_out = off_device(batch_out)
                loss = tweezer.get(batch_out, 'loss')
                if loss is None:
                    raise RuntimeError('val_step should return loss')
                losses.append(loss)
                batch_outs.append(batch_out)
                targets.append(off_device(batch.target))

                batches.set_postfix({'loss': f"{loss:.4f}", 'ts': self.state.ts})
                self.update_progress_state(batches)
                self.callback_handler.on_val_batch_end()

        self.state.set_metric('loss/val', sum(losses) / len(losses))
        self.compute_metrics(batch_outs, targets)
        self.callback_handler.on_val_epoch_end()

    def update_progress_state(self, pbar):
        n = pbar.n
        total = pbar.total
        _rate = pbar.format_dict.get('rate')
        unit = pbar.unit
        if _rate:
            rate = f"{_rate:5.2f}{unit}/s" if _rate >= 1 else f"{_rate:5.2f}s/{unit}"
        else:
            rate = '?/s'
        remain = pbar.format_interval((total - n) / _rate) if _rate else '?'
        postfix = pbar.postfix
        self.state.progress.update({
            'n': n,
            'total': total,
            'rate': rate,
            'remain': remain,
            'postfix': postfix,
        })

    def compute_metrics(self, outs, targets):
        metrics = self.model.compute_metrics(outs, targets)
        if metrics:
            self.state.set_metrics(metrics)
            if self.trainer_conf.measure is None:
                self.trainer_conf.measure = tweezer.guess_measure_name(metrics)
                if self.trainer_conf.measure is None:
                    LOGGER.warning('Failed to guess a measure metric name')

    def lr_scheduler_step(self):
        scheduler_args = {}
        if (metrics_monitor := self.scheduler_conf.monitor) is not None:
            scheduler_args['metrics'] = self.state.metrics.get(metrics_monitor)
        hao.invoker.invoke(self.scheduler.step, **scheduler_args)

        # get the new lrs
        lrs = self.get_lrs()
        self.state.set_metrics({'lr': lrs[0], 'lrs': lrs})

    def log_metrics(self):
        width = max(len(k) for k, _ in self.state.metrics.items()) + 1
        metrics = '\n'.join([f"\t{k: <{width}}: {v}" for k, v in self.state.metrics.items()])
        LOGGER.info(f"{' metrics '.center(50, '━')}\n{metrics}")
        for k, v in self.state.reports.items():
            LOGGER.info(f"{f' {k} '.center(50, '━')}\n{v}")
        self.update_score()

    def update_score(self):
        if self.trainer_conf.measure is not None and (score := self.state.metrics.get(self.trainer_conf.measure)) is not None:
            self.state.score.clear()
            self.state.score[self.trainer_conf.measure] = score

    def save_if_should(self):
        if self.state._ckpts.should_save:
            self.state._ckpts.path_new = self.save()
            self.callback_handler.on_save_checkpoint()
            self.state._ckpts.should_save = False

    def save(self, name: str | None = None, *, is_last: bool = False):
        state_dicts = {
            'state': {'epoch': self.state.epoch},
            'train_conf': self.train_conf,
            'model_conf': self.model.model_conf,
            'optimizer_state_dict': self.optimizer.state_dict(),
            'scheduler_state_dict': self.scheduler.state_dict(),
        }
        if (peft_config := getattr(self.model, 'peft_config', None)) is None:
            self.model.on_save_checkpoint()
            state_dicts['state_dict'] = self.model.state_dict()
        else:
            state_dicts['state_dict'] = get_peft_model_state_dict(self.model)
            state_dicts['peft_config'] = {**peft_config.__dict__ , 'inference_mode': True}

        if self.scaler:
            state_dicts['scaler_state_dict'] = self.scaler.state_dict()
        params = {
            'model': self.train_conf.model,
            'dataset': self.train_conf.dataset,
            'exp': self.trainer_conf.exp or 'na',
            'epoch': self.state.epoch,
            'ts': self.state.ts,
            **{k.replace('/', '_'): f"{v:.4f}" for k, v in self.state.metrics.items() if isinstance(v, (str, int, float, bool))},
        }
        checkpoint_name = name or self.trainer_conf.checkpoint_name
        if self.trainer_conf.measure is not None:
            checkpoint_name = Template(checkpoint_name).safe_substitute({'measure': self.trainer_conf.measure})
        else:
            checkpoint_name = checkpoint_name.replace('-${measure}={${measure}}', '')
        try:
            filename = checkpoint_name.format(**params)
        except Exception:
            filename = "{model}-{dataset}-{exp}-{ts}-epoch={epoch}.ckpt".format(**params)

        if is_last:
            base, ext = os.path.splitext(filename)
            filename = f"{base}-last{ext}"
        filepath = f"data/checkpoints/{filename}"
        fullpath = hao.paths.get(filepath)
        hao.paths.make_parent_dirs(fullpath)
        torch.save(state_dicts, fullpath)
        LOGGER.debug(f"saved checkpoint: {filepath}")
        return filepath

    def save_model(self):
        if self.state.epoch <= 0 or len(self.state._ckpts.top_n) == 0:
            return
        checkpoint_path = self.state._ckpts.top_n[0].get('path')
        if not os.path.isfile(checkpoint_path):
            return
        filebase, _ = os.path.splitext(os.path.basename(checkpoint_path))
        filepath = f"data/model/{filebase}.bin"
        fullpath = hao.paths.get(filepath)
        if (peft_config := getattr(self.model, 'peft_config', None)) is None:
            self.model.export_to_model(fullpath)
        else:
            state_dicts = {
                'model_conf': self.model.model_conf,
                'state_dict': get_peft_model_state_dict(self.model),
                'peft_config': {**peft_config.__dict__ , 'inference_mode': True},
            }
            hao.paths.make_parent_dirs(fullpath)
            torch.save(state_dicts, fullpath)
        LOGGER.info(f"saved model: {filepath}")
