# -*- coding: utf-8 -*-
import asyncio
import json
import os
from collections import defaultdict
from contextlib import asynccontextmanager
from datetime import datetime

import hao
import uvicorn
from fastapi import Depends, FastAPI, Query, Request, Response, WebSocket
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.staticfiles import StaticFiles
from hao.namespaces import attr, from_args
from hao.sqlite import SQLite
from starlette.exceptions import HTTPException
from starlette.websockets import WebSocketDisconnect
from websockets.exceptions import ConnectionClosed, ConnectionClosedOK

from tailors import __version__
from tailors.trainer.ui import runner

from .auths import TOKEN_KEY, Authed, encode_user
from .domains import User
from .exceptions import ExpiredTokenException, InvalidUserOrPasswordException, UnAuthedException
from .scheduled import scheduler
from .utils import JSON_FIELDS_TASK, JSON_FIELDS_TASK_EPOCH, SQLITE_PATH, convert_json, tail_f

LOGGER = hao.logs.get_logger('tailors.ui')
ACCESS = hao.logs.get_logger('access')


@from_args(config='~/.tailors.yml')
class Conf:
    host: str = attr(str, key='host', default='0.0.0.0')
    port: int = attr(int, key='port', default=8050)
    username: str = attr(str, key='username', default='tailors')
    password: str = attr(str, key='password')


_CONF = Conf()


@asynccontextmanager
async def lifespan(_app: FastAPI):
    if _CONF.password is None:
        _CONF.password = hao.strings.random(10)
    LOGGER.warning((
        'tailors ui started\n'
        f"\thost    : {_CONF.host}\n"
        f"\tport    : {_CONF.port}\n"
        f"\tusername: {_CONF.username}\n"
        f"\tpassword: {_CONF.password}\n"
    ))
    scheduler.start()
    yield
    LOGGER.warning('tailors ui stopped')


app = FastAPI(title='Tailors UI', version=__version__, lifespan=lifespan)
app.add_middleware(GZipMiddleware, minimum_size=1000)
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True, allow_methods=['*'], allow_headers=['*'])


@app.get('/_ping')
async def handle_ping():
    return {'msg': f"Tailors UI is running, version: {__version__}"}


@app.get('/api/version')
async def handle_version():
    return {'data': {'version': __version__}}


@app.post('/api/login')
async def handle_login(response: Response, form: OAuth2PasswordRequestForm = Depends()):
    user = User(username=form.username, password=form.password)
    if user.username != _CONF.username or user.password != _CONF.password:
        raise InvalidUserOrPasswordException()
    token = encode_user(user)
    # response.set_cookie(key=TOKEN_KEY, value=token, max_age=TOKEN_TTL_SECONDS, httponly=True)
    return {'data': {'token': token, 'token_type': 'bearer'}}


@app.get('/api/logout')
async def handle_logout(response: Response):
    token = None
    response.delete_cookie(key=TOKEN_KEY)
    return {'msg': 'You are logged out', 'data': {'token': token, 'token_type': 'bearer'}}


@app.get('/api/tasks')
async def handle_get_tasks(user: User = Depends(Authed())):
    with SQLite(path=SQLITE_PATH, cursor='dict') as db:
        sql = (
            'select * from ('
            ' select task, count(task) as count, start from ('
            '  select * from tasks where deleted != 1 order by start desc'
            ' ) group by task '
            ') order by start desc'
        )
        tasks = db.execute(sql).fetchall()
    return {'data': tasks}


@app.get('/api/task/{task}')
async def handle_get_task(task: str, ts: list[str] | None = Query(default=None), deleted: bool = False, user: User = Depends(Authed())):
    if ts is None:
        sql = 'select * from tasks where task = ? and deleted == ? order by start desc'
        params = (task, deleted)
    else:
        sql = f"select * from tasks where task = ? and deleted == ? ts in ({','.join('?'*len(ts))}) order by start desc"
        params = (task, deleted, *ts)

    with SQLite(path=SQLITE_PATH, cursor='dict') as db:
        tasks = db.execute(sql, params).fetchall()

    for _task in tasks:
        convert_json(_task, JSON_FIELDS_TASK)
        start, end = _task.get('start'), _task.get('end')
        if end is None:
            _task['status'] = 'in progress'
        else:
            start, end = datetime.fromisoformat(start), datetime.fromisoformat(end)
            _task['status'] = f"{hao.dates.pretty_time_delta((end - start).seconds, millis=False)}"
    return {'data': tasks}


@app.get('/api/chartdata/{task}')
async def handle_get_task_chartdata(task: str, ts: list[str] | None = Query(default=None), user: User = Depends(Authed())):
    datasets, groups, epochs, sources, times = {}, defaultdict(set), set(), defaultdict(list), defaultdict(list)
    if ts is None:
        return {'data': {'groups': groups, 'datasets': datasets}}

    sql = 'select * from tasks_epoch where task = ? and ts = ?'
    with SQLite(path=SQLITE_PATH, cursor='dict') as db:
        for _ts in ts:
            items = db.execute(sql, (task, _ts)).fetchall()
            if not items:
                datasets[_ts] = {}
                continue

            metrics = defaultdict(list)
            for item in items:
                convert_json(item, JSON_FIELDS_TASK_EPOCH)
                for key, val in item.get('metrics').items():
                    if isinstance(val, list):
                        continue
                    metrics[key].append(val)
                    splits = key.split('/')
                    groups[splits[0]].add(key)
                timestamp, relative = item.get('timestamp'), item.get('relative') or '-'
                times[_ts].append(f"{hao.dates.formatted(timestamp)} ({relative})")
                epochs.add(item.get('epoch'))
            # metrics = dict(sorted(metrics.items()))
            for key, values in metrics.items():
                sources[key].append([_ts] + values)
    groups = dict(sorted([(k, sorted(v)) for k, v in groups.items()]))
    epochs = ['epoch'] + list(sorted(epochs))

    datasets = {
        _key: {'source': [epochs] + _source}
        for _key, _source in sources.items()
    }

    return {'data': {'groups': groups, 'datasets': datasets, 'times': times}}


@app.delete('/api/task/{task}/{ts}')
async def handle_delete_task(task: str, ts: str, user: User = Depends(Authed())):
    with SQLite(path=SQLITE_PATH, cursor='dict') as db:
        sql = 'update tasks set deleted = 1 where task = ? and ts = ?'
        db.execute(sql, (task, ts), commit=True)
        return {'data': None, 'msg': f"[{ts}] deleted"}


@app.post('/api/task/{task}/{ts}/restore')
async def handle_restore_task(task: str, ts: str, user: User = Depends(Authed())):
    with SQLite(path=SQLITE_PATH, cursor='dict') as db:
        sql = 'update tasks set deleted = 0 where task = ? and ts = ?'
        db.execute(sql, (task, ts), commit=True)
        return {'data': None, 'msg': f"[{ts}] restored"}


@app.post('/api/task/start')
async def handle_start_task(request: Request, user: User = Depends(Authed())):
    args = await request.json()
    task = args.pop('task', None)
    if task is None:
        return {'msg': 'missing arg: task'}
    ts, pid = runner.start(task, args)
    LOGGER.info(f"[start-task] task: {task}, ts: {ts}, pid: {pid}")
    return {'data': {'ts': ts, 'pid': pid}, 'msg': f"[{task}] triggered {ts}, pid: {pid}"}


@app.websocket("/task/logs")
async def handle_ws(websocket: WebSocket):
    async def logs_task(path, queue: asyncio.Queue, event: asyncio.Event):
        logs = tail_f(path)
        while not event.is_set():
            try:
                line = next(logs)
                if line:
                    line = line.rstrip()
                    queue.put_nowait({'log': line})
                else:
                    await asyncio.sleep(1)
            except Exception as e:
                LOGGER.exception(e)

    async def progress_task(queue: asyncio.Queue, event: asyncio.Event):
        sql = 'select progress, end from tasks where task = ? and ts = ?'
        with SQLite(path=SQLITE_PATH, cursor='tuple') as db:
            while not event.is_set():
                try:
                    progress, end = db.execute(sql, (task, ts)).fetchone()
                    if progress:
                        queue.put_nowait(json.loads(progress))
                    if end is not None:
                        await asyncio.sleep(5)
                        event.set()
                        break
                    await asyncio.sleep(1)
                except Exception as e:
                    LOGGER.exception(e)

    async def sender_task(queue: asyncio.Queue, event: asyncio.Event):
        while not event.is_set():
            try:
                item = queue.get_nowait()
                queue.task_done()
                if item:
                    await websocket.send_text(hao.jsons.dumps(item))
                else:
                    await asyncio.sleep(1)
            except asyncio.queues.QueueEmpty:
                await asyncio.sleep(1)
            except (ConnectionClosed, ConnectionClosedOK):
                event.set()
                break
            except Exception as e:
                LOGGER.exception(e)

    await websocket.accept()
    data = await websocket.receive_text()
    LOGGER.info(f"[ws] {data}")
    await websocket.send_json({'msg': 'test'})
    if not data:
        await websocket.send_text(hao.jsons.dumps({'msg': 'invalid request'}))
        await websocket.close()
        return
    data = json.loads(data)
    task, ts = data.get('task'), data.get('ts')

    try:
        log_path = hao.paths.get(f"data/logs/{task}/{ts}.log")
        if not os.path.exists(log_path):
            await websocket.send_text(hao.jsons.dumps({'msg': f"Log file not found: data/logs/{task}/{ts}.log"}))
            await websocket.close()
            return

        q, e = asyncio.Queue(), asyncio.Event()
        await asyncio.gather(
            logs_task(log_path, q, e),
            progress_task(q, e),
            sender_task(q, e),
        )
        await websocket.close()
        LOGGER.info(f"[ws] {data} done")
    except asyncio.CancelledError as e:
        LOGGER.exception(e)
        pass
    except (WebSocketDisconnect, ConnectionClosed, RuntimeError):
        LOGGER.debug('[ws] disconnected')


app.mount('/', StaticFiles(packages=['tailors.trainer.ui'], html=True), name='static')


@app.exception_handler(404)
@app.exception_handler(InvalidUserOrPasswordException)
@app.exception_handler(UnAuthedException)
@app.exception_handler(ExpiredTokenException)
@app.exception_handler(Exception)
async def handle_exceptions(request: Request, ex: Exception):
    base_url, url = str(request.base_url), str(request.url)
    url = url[len(base_url) - 1:]
    msg, code = str(ex), 200

    if isinstance(ex, HTTPException):
        msg = ex.detail
    elif isinstance(ex, RequestValidationError):
        msg = '; '.join([f"[{e._loc[-1]}] {e.exc.msg_template}" for e in ex.raw_errors])
    elif isinstance(ex, (UnAuthedException, ExpiredTokenException)):
        code = 401

    return JSONResponse(status_code=code, content={'error': msg})


def run():
    try:
        uvicorn.run(app, host=_CONF.host, port=_CONF.port, server_header=False, access_log=False)
    except KeyboardInterrupt:
        print('[ctrl-c]')
    except Exception as err:
        LOGGER.exception(err)


if __name__ == '__main__':
    run()
