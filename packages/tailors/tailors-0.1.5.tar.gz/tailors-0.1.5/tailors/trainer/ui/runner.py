import os
import shlex
from datetime import datetime
from subprocess import DEVNULL, Popen


def start(task: str, args: dict):
    ts = datetime.now().strftime('%y%m%d-%H%M')
    command = ' '.join(
        ['python -m tailors.trainer.train', f"--task={task}", f"--ts={ts}"] +
        [f"--{key}={val}" for key, val in args.items() if key not in ('ts',) and val not in (None, 'null')]
    )
    process = Popen(shlex.split(command), stdout=DEVNULL, stderr=DEVNULL, preexec_fn=os.setpgrp)
    return ts, process.pid
