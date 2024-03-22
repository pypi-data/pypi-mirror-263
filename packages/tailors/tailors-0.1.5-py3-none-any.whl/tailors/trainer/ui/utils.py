import json
import os
import time

SQLITE_PATH = 'data/tailors.db'
JSON_FIELDS_TASK = ('train_conf', 'trainer_conf', 'model_conf', 'dataset_conf', 'optimizer_conf', 'scheduler_conf', 'params', 'metrics', 'reports', 'checkpoints')
JSON_FIELDS_TASK_EPOCH = ('metrics', 'reports')


def convert_json(obj: dict, fields: list[str]):
    def convert_nan_inf(_val):
        return .0 if _val != _val or _val == float('inf') else _val

    if obj is None or fields is None or len(fields) == 0:
        return
    for field in fields:
        if (val := obj.get(field)) is None:
            continue
        try:
            obj[field] = {k: convert_nan_inf(v) for k, v in json.loads(val).items()}
        except Exception:
            pass


def tail_f(path: str):
    line = ''
    with open(path) as f:
        while True:
            tmp = f.readline()
            if tmp:
                line += tmp
                if line.endswith('\n'):
                    yield line
                    line = ''
                # time.sleep(0.1)
            else:
                time.sleep(1)
                yield None
