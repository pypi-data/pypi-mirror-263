# -*- coding: utf-8 -*-
import sys
import warnings
from datetime import datetime

import hao
import regex

from tailors.trainer.exceptions import TailorsTrainerError
from tailors.trainer.trainer import TaskConf, Trainer

warnings.filterwarnings("ignore")
LOGGER = hao.logs.get_logger('train')


def parse_args() -> dict:
    args_str = ' '.join(sys.argv[1:])
    args = [regex.compile(r'(?:\s*=\s*|\s+)').split(item) for item in regex.compile(r'\s*\-{2}').split(args_str) if item]
    return {a[0]: a[1] if len(a) == 2 else None for a in args}


def log_cmdline():
    arguments = [f"--{k}={v}" if v else f"--{k}" for k, v in parse_args().items()]
    n_args = len(arguments)

    sep = ' ' if n_args <= 1 else ' \\\n\t'
    args = sep.join(arguments)
    LOGGER.info(f"\n{'━' * 50}\ntailors-train{sep}{args}\n{'━' * 50}")


def load_task(task_conf: TaskConf | None = None):
    task_conf = task_conf or TaskConf()
    if task_conf.task is None:
        return
    task = hao.config.get(f"tasks.{task_conf.task}", config='tailors.yml')
    if task is None or len(task) == 0:
        return
    ts = datetime.now().strftime('%y%m%d-%H%M')
    args = parse_args()
    arguments = [f"--{k}={v}" for k, v in task.items() if k not in args and v]
    sys.argv.extend(arguments + [f"--ts={ts}"])
    hao.logs.add_log_to_file(f"data/logs/{task_conf.task}/{ts}.log")


def train(task_conf: TaskConf | None = None):
    try:
        if task_conf is None:
            log_cmdline()
        load_task(task_conf)
        trainer = Trainer()
        trainer.fit()
    except KeyboardInterrupt:
        print("[ctrl-c] stopped")
    except TailorsTrainerError as err:
        LOGGER.error(err)
    except Exception as err:
        LOGGER.exception(err)


if __name__ == "__main__":
    train()
