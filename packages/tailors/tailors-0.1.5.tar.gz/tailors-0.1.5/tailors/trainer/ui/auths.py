import asyncio
import time

import hao
from decorator import decorator
from fastapi import Depends, Request
from fastapi.responses import RedirectResponse
from jose import JWTError, jwt
from passlib.context import CryptContext

from .domains import User
from .exceptions import BadTokenException, ExpiredTokenException, UnAuthedException
from .unsecure import UnsecureBearer

TOKEN_KEY = 'tailors-token'
SECRET = hao.config.get('app.secret', 'M4GpDND3TGHB')
_PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")
_ALGORITHM = "HS256"
TOKEN_TTL_SECONDS = 3600 * 24 * 7

_BEARER = UnsecureBearer(token_key=TOKEN_KEY, token_url='api/login', scheme_name='JWT', auto_error=False)


def current_user(token: str = Depends(_BEARER)):
    return decode_user(token)


class Authed:
    def __call__(self, user: User = Depends(current_user)):
        pass


def get_hashed_password(password: str) -> str:
    return _PWD_CONTEXT.hash(password)


def verify_password(password: str, hashed_pass: str) -> bool:
    return _PWD_CONTEXT.verify(password, hashed_pass)


def encode_token(data):
    return jwt.encode(data, SECRET, _ALGORITHM)


def decode_token(token):
    try:
        return jwt.decode(token, SECRET, algorithms=[_ALGORITHM])
    except JWTError:
        raise BadTokenException()


def encode_user(user: User):
    return encode_token(user.model_dump(exclude_none=True))


def decode_user(token):
    if token is None:
        raise UnAuthedException()
    user = User(**decode_token(token))
    if user.timestamp is None or user.timestamp < (time.time() - TOKEN_TTL_SECONDS):
        raise ExpiredTokenException()
    return user


@decorator
async def auth(func, *args, **kw):
    request = args[0]

    token = request.cookies.get(TOKEN_KEY)

    if token is None:
        if '/api' in str(request.url):
            return {'msg': 'You are NOT logged in, login required'}
        else:
            return RedirectResponse(url='/login')

    if asyncio.iscoroutinefunction(func):
        return await func(*args, **kw)
    else:
        return func(*args, **kw)


def get_username(request: Request):
    token = request.cookies.get(TOKEN_KEY)
    if not token:
        return None

    token_data = decode_token(token)
    return token_data.get('username')
