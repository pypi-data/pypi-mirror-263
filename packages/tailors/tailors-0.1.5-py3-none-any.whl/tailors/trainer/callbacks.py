# -*- coding: utf-8 -*-
import os
from abc import ABC
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from sqlite3 import IntegrityError

import hao
import pandas as pd
from hao.args import args_as_dict
from hao.sqlite import SQLite

from tailors import trainer
from tailors.domains import Derivable
from tailors.utils import tweezer

from .exceptions import StopTailorsTrainer

LOGGER = hao.logs.get_logger('trainer.callbacks')


class Callback(ABC, Derivable):

    def __init__(self, trainer: 'trainer.trainer.Trainer') -> None:
        super().__init__()
        self.trainer = trainer

    def on_fit_start(self):
        pass

    def on_fit_end(self):
        pass

    def on_epoch_start(self):
        pass

    def on_epoch_end(self):
        pass

    def on_train_epoch_start(self, epoch):
        pass

    def on_train_epoch_end(self, epoch):
        pass

    def on_val_epoch_start(self):
        pass

    def on_val_epoch_end(self):
        pass

    def on_train_batch_start(self):
        pass

    def on_train_batch_end(self, epoch, batch, batch_out):
        pass

    def on_val_batch_start(self):
        pass

    def on_val_batch_end(self):
        pass

    def on_save_checkpoint(self):
        pass

    def load_state_dict(self, state_dict):
        pass

    @property
    def task(self):
        return self.trainer.task_conf.task

    @property
    def train_conf(self):
        return self.trainer.train_conf

    @property
    def trainer_conf(self):
        return self.trainer.trainer_conf

    @property
    def model_conf(self):
        return self.trainer.model_conf

    @property
    def dataset_conf(self):
        return self.trainer.dataset_conf

    @property
    def optimizer_conf(self):
        return self.trainer.optimizer_conf

    @property
    def scheduler_conf(self):
        return self.trainer.scheduler_conf

    @property
    def state(self):
        return self.trainer.state

    @property
    def exp_dir(self):
        return self.trainer.exp_dir


class CallbackHandler:

    def __init__(self, trainer: 'trainer.trainer.Trainer', callbacks: list[Callback] | None = None) -> None:
        self.callbacks = [
            clz(trainer)
            for clz in callbacks or [
                TensorboardLoggerCallback,
                TailorsLoggerCallback,
                EarlyStopCallback,
                CheckpointCallback,
            ]
        ]
        LOGGER.info(f"callbacks: {[f'{c.__class__.__name__}' for c in self.callbacks]}")

    def _on_event(self, event: str, **kwargs):
        for callback in self.callbacks:
            fn = getattr(callback, event, None)
            if fn is None:
                continue
            hao.invoker.invoke(fn, **kwargs)

    def on_fit_start(self):
        self._on_event('on_fit_start')

    def on_fit_end(self):
        self._on_event('on_fit_end')

    def on_epoch_start(self):
        self._on_event('on_epoch_start')

    def on_epoch_end(self):
        self._on_event('on_epoch_end')

    def on_train_epoch_start(self, epoch: int):
        self._on_event('on_train_epoch_start', epoch=epoch)

    def on_train_epoch_end(self, epoch: int):
        self._on_event('on_train_epoch_end', epoch=epoch)

    def on_val_epoch_start(self):
        self._on_event('on_val_epoch_start')

    def on_val_epoch_end(self):
        self._on_event('on_val_epoch_end')

    def on_train_batch_start(self):
        self._on_event('on_train_batch_start')

    def on_train_batch_end(self, epoch, batch, batch_out):
        self._on_event('on_train_batch_end', epoch=epoch, batch=batch, batch_out=batch_out)

    def on_val_batch_start(self):
        self._on_event('on_val_batch_start')

    def on_val_batch_end(self):
        self._on_event('on_val_batch_end')

    def on_save_checkpoint(self):
        self._on_event('on_save_checkpoint')

    def load_state_dict(self, state_dict):
        self._on_event('load_state_dict', state_dict)


class TensorboardLoggerCallback(Callback):
    def __init__(self, trainer: 'trainer.trainer.Trainer') -> None:
        super().__init__(trainer)
        self.path = hao.paths.get(self.exp_dir)
        self.writer = None

    def write_scalar(self, k, v, step=None):
        if not isinstance(v, (int, float)):
            return
        if step is None:
            step = self.state.step
        if self.writer is None:
            from torch.utils.tensorboard import SummaryWriter
            self.writer = SummaryWriter(self.path)
        self.writer.add_scalar(k, v, step)

    def on_train_batch_end(self, epoch, batch, batch_out):
        self.write_scalar('loss/batch', self.state.metrics.get('loss/batch'))

    def on_epoch_end(self):
        for k, v in self.state.metrics.items():
            self.write_scalar(k, v)


class WandbLoggerCallback(Callback):
    def __init__(self, trainer: 'trainer.trainer.Trainer') -> None:
        super().__init__(trainer)
        try:
            import wandb
        except ImportError:
            os.system('pip install wandb')
            import wandb
        self.wandb = wandb

    def on_fit_start(self):
        self.wandb.init(
            project=self.task,
            name=self.state.ts,
            config=args_as_dict()
        )

    def on_fit_end(self):
        self.wandb.finish()

    def on_train_batch_end(self, epoch, batch, batch_out):
        self.wandb.log({'loss/batch': self.state.metrics.get('loss/batch')})

    def on_epoch_end(self):
        for k, v in self.state.metrics.items():
            self.wandb.log({k: v})


class TailorsLoggerCallback(Callback):
    def __init__(self, trainer: 'trainer.trainer.Trainer') -> None:
        super().__init__(trainer)
        self.path = hao.paths.get('data', 'tailors.db')

    def _create_tasks_table(self):
        sql = (
            'CREATE TABLE IF NOT EXISTS tasks ('
            '  task TEXT NOT NULL,'
            '  ts TEXT NOT NULL,'
            '  model TEXT,'
            '  dataset TEXT,'
            '  train_conf TEXT,'
            '  trainer_conf TEXT,'
            '  model_conf TEXT,'
            '  dataset_conf TEXT,'
            '  optimizer_conf TEXT,'
            '  scheduler_conf TEXT,'
            '  params TEXT,'
            '  progress TEXT,'
            '  metrics TEXT,'
            '  reports TEXT,'
            '  comment TEXT,'
            '  start TEXT,'
            '  end TEXT,'
            '  checkpoints TEXT,'
            '  deleted INTEGER DEFAULT 0,'
            '  CONSTRAINT tasks_pk PRIMARY KEY (ts)'
            ')'
        )
        self._execute(sql)

    def _create_tasks_epoch_table(self):
        sql = (
            'CREATE TABLE IF NOT EXISTS tasks_epoch ('
            '  task TEXT NOT NULL,'
            '  ts TEXT NOT NULL,'
            '  epoch INTEGER,'
            '  metrics TEXT,'
            '  reports TEXT,'
            '  timestamp TEXT,'
            '  relative TEXT'
            ')'
        )
        self._execute(sql)

    def _add_task(self):
        sql = (
            'INSERT INTO tasks '
            '(task, ts, model, dataset, train_conf, trainer_conf, model_conf, dataset_conf, optimizer_conf, scheduler_conf, params, start) '
            'VALUES '
            '(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
        )
        task = self.task
        ts = self.state.ts
        model = self.train_conf.model
        dataset = self.train_conf.dataset
        train_conf = hao.jsons.dumps(self.train_conf)
        trainer_conf = hao.jsons.dumps(self.trainer_conf)
        model_conf = hao.jsons.dumps(self.model_conf)
        dataset_conf = hao.jsons.dumps(self.dataset_conf)
        optimizer_conf = hao.jsons.dumps(self.optimizer_conf)
        scheduler_conf = hao.jsons.dumps(self.scheduler_conf)
        params = hao.jsons.dumps({k: v for k, v in args_as_dict().items() if k not in ('log-to',)})
        start = datetime.now().isoformat()
        vals = (task, ts, model, dataset, train_conf, trainer_conf, model_conf, dataset_conf, optimizer_conf, scheduler_conf, params, start)
        try:
            self._execute(sql, vals)
        except IntegrityError:
            sql = (
                'UPDATE tasks '
                'SET model=?, dataset=?, train_conf=?, trainer_conf=?, model_conf=?, dataset_conf=?, optimizer_conf=?, scheduler_conf=?, params=?, start=? '
                'WHERE task=? and ts=?'
            )
            vals = (model, dataset, train_conf, trainer_conf, model_conf, dataset_conf, optimizer_conf, scheduler_conf, params, start, task, ts)
            self._execute(sql, vals)

    def _end_task(self):
        sql = 'UPDATE tasks SET metrics=?, reports=?, end=?, checkpoints=? where task=? and ts=?'
        metrics = hao.jsons.dumps(self.state.metrics)
        reports = hao.jsons.dumps(self.state.reports)
        checkpoints = hao.jsons.dumps({
            'top_n': self.state._ckpts.top_n,
            'last': self.state._ckpts.last,
        })
        vals = (metrics, reports, datetime.now().isoformat(), checkpoints, self.task, self.state.ts)
        self._execute(sql, vals)

    def _update_task_progress(self):
        sql = 'UPDATE tasks SET progress=? where task=? and ts=?'
        progress = hao.jsons.dumps(self.state.progress)
        vals = (progress, self.task, self.state.ts)
        self._execute(sql, vals)

    def _add_task_epoch(self):
        sql = 'INSERT INTO tasks_epoch (task, ts, epoch, metrics, reports, timestamp, relative) VALUES (?, ?, ?, ?, ?, ?, ?)'
        epoch = self.state.epoch
        metrics = hao.jsons.dumps(self.state.metrics)
        reports = hao.jsons.dumps(self.state.reports)
        timestamp = datetime.now().isoformat()
        relative = self.state.took
        vals = (self.task, self.state.ts, epoch, metrics, reports, timestamp, relative)
        self._execute(sql, vals)

    def on_fit_start(self):
        self._create_tasks_table()
        self._create_tasks_epoch_table()
        self._add_task()

    def on_fit_end(self):
        self._end_task()

    def on_train_batch_end(self, *args, **kwargs):
        self._update_task_progress()

    def on_val_batch_end(self, *args, **kwargs):
        self._update_task_progress()

    def on_epoch_end(self):
        self._add_task_epoch()

    def _execute(self, sql: str, params: tuple | None = None):
        with SQLite(path=self.path) as db:
            return db.execute(sql, params, commit=True)


class EarlyStopCallback(Callback):
    def __init__(self, trainer: 'trainer.trainer.Trainer') -> None:
        super().__init__(trainer)
        self.consec_increases = 0

    def should_stop(self):
        if self.state.epoch < 1 or len(self.state.val_losses) < 2:
            return False
        if self.state.val_losses[-1] <= self.state.val_losses[-2]:
            self.consec_increases = 0
            return False
        self.consec_increases += 1
        return self.consec_increases >= self.trainer_conf.early_stop_patience

    def on_epoch_end(self):
        if self.should_stop():
            LOGGER.info(f"[early-stop] val loss increased for {self.consec_increases} consecutive epochs")
            raise StopTailorsTrainer()


class CheckpointCallback(Callback):

    def on_epoch_end(self):
        if any(v < 0.3 for k, v in self.state.metrics.items() if 'f1' in k):
            return
        if len(self.state._ckpts.top_n) == 0 or self.trainer_conf.save_last or self.state.val_losses[-1] <= self.state._ckpts.top_n[0].get('loss'):
            self.state._ckpts.should_save = True

    def on_save_checkpoint(self):
        path_new = self.state._ckpts.path_new
        if path_new is None:
            return

        to_deletes = []
        if len(self.state._ckpts.top_n) == 0 or self.state.val_losses[-1] <= self.state.val_losses[-2]:
            i = self.get_insert_index()
            self.state._ckpts.top_n.insert(i, {
                'epoch': self.state.epoch,
                'loss': self.state.val_losses[-1],
                'score': self.state.score,
                'path': path_new,
                'name': Path(path_new).name,
            })
            while len(self.state._ckpts.top_n) > self.trainer_conf.save_top_n:
                top = self.state._ckpts.top_n.pop()
                to_deletes.append(top.get('path'))
        if self.trainer_conf.save_last:
            if self.state._ckpts.last and all(self.state._ckpts.last != top.get('path') for top in self.state._ckpts.top_n):
                to_deletes.append(self.state._ckpts.last)
            self.state._ckpts.last = path_new
        for to_delete in to_deletes:
            path = hao.paths.get(to_delete)
            if os.path.isfile(path):
                os.remove(path)

        LOGGER.info(self.top_n_msg())

    def on_fit_end(self):
        LOGGER.info(self.top_n_msg())
        if self.trainer_conf.save_last:
            LOGGER.info(f"[checkpoint] last: {self.state._ckpts.last}")

    def top_n_msg(self):
        if len(self.state._ckpts.top_n) == 0:
            top_n = 'n/a'
        else:
            top_n = ''.join([f"\n\t[{i}] {top.get('name')}" for i, top in enumerate(self.state._ckpts.top_n)])
        return f"[checkpoint] top {self.trainer_conf.save_top_n}: {top_n}"

    def get_insert_index(self):
        if len(self.state._ckpts.top_n) == 0:
            return 0
        val_loss = self.state.val_losses[-1]
        for i, top in enumerate(self.state._ckpts.top_n):
            if val_loss <= top.get('loss'):
                return i
        return i + 1


class DynamicsCallback(Callback):
    def __init__(self, trainer: 'trainer.trainer.Trainer') -> None:
        super().__init__(trainer)
        self.dynamics = defaultdict(list)

    def on_train_batch_end(self, epoch, batch, batch_out):
        logits = tweezer.get(batch_out, ['logit', 'logits'])
        if logits is None:
            return
        logits = logits.detach().cpu().tolist()
        target = batch.target.detach().cpu().tolist()
        for guid, logits, gold in zip(batch.idx, logits, target):
            self.dynamics['epoch'].append(epoch)
            self.dynamics['guid'].append(guid)
            self.dynamics['logits'].append(logits)
            self.dynamics['gold'].append(gold)

    def on_train_epoch_end(self, epoch):
        if len(self.dynamics) == 0:
            return
        path = f"{self.exp_dir}/dynamics-{epoch:0>2}.pkl"
        hao.paths.make_parent_dirs(hao.paths.get(path))
        df = pd.DataFrame(self.dynamics)
        df.to_pickle(path)
