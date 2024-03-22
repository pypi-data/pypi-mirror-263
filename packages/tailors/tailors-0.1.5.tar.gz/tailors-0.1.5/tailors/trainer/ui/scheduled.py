# -*- coding: utf-8 -*-
import os
from datetime import datetime, timedelta

import hao
from apscheduler.schedulers.background import BackgroundScheduler
from hao.sqlite import SQLite

from .utils import JSON_FIELDS_TASK, SQLITE_PATH, convert_json

LOGGER = hao.logs.get_logger(__name__)


scheduler = BackgroundScheduler({
    'apscheduler.executors.default': {
        'class': 'apscheduler.executors.pool:ThreadPoolExecutor',
        'max_workers': '2'
    },
    'apscheduler.executors.processpool': {
        'type': 'processpool',
        'max_workers': '3'
    },
    'apscheduler.job_defaults.coalesce': 'true',
    'apscheduler.job_defaults.max_instances': '1',
    'apscheduler.timezone': 'Asia/Shanghai',
})


@scheduler.scheduled_job('cron', id='clean-task-epochs', hour=0, minute=0, second=0, max_instances=1, coalesce=True)
def schedule_clean_task_epochs():
    def remove_file(path):
        try:
            os.remove(path)
        except Exception:
            pass

    a_week_ago = hao.dates.formatted(datetime.now() - timedelta(days=7))
    with SQLite(path=SQLITE_PATH, cursor='dict') as db:
        sql_fetch = 'select * from tasks where deleted = 1 and (end < ? or end is null)'
        tasks = db.execute(sql_fetch, (a_week_ago,)).fetchall()
        if tasks is None:
            return
        sql_delete = 'delete from tasks where deleted = 1 and (end < ? or end is null)'
        db.execute(sql_delete, (a_week_ago, ), commit=True)

        for task in tasks:
            convert_json(task, JSON_FIELDS_TASK)
            db.execute('delete from tasks_epoch where task = ? and ts = ?', (task.get('task'), task.get('ts')), commit=True)

            checkpoints = task.get('checkpoints')  # {'top_n': [], 'last': ''}
            if checkpoints:
                if (top_n := checkpoints.get('top_n')) is not None:
                    for top in top_n:
                        remove_file(hao.paths.get(top.get('path')))
                if (last := checkpoints.get('last')) is not None:
                    remove_file(hao.paths.get(last))
            remove_file(hao.paths.get(f"data/logs/{task.get('task')}/{task.get('ts')}.log"))

