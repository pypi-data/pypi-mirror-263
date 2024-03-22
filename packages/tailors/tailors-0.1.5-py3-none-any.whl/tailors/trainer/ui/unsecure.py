from fastapi import Request
from fastapi.security import OAuth2PasswordBearer


class UnsecureBearer(OAuth2PasswordBearer):

    def __init__(self,
                 token_url: str,
                 token_key: str,
                 scheme_name: str | None = None,
                 scopes: dict[str, str] | None = None,
                 description: str | None = None,
                 auto_error: bool = True):
        super().__init__(token_url, scheme_name, scopes, description, auto_error)
        self.token_key = token_key

    async def __call__(self, request: Request) -> str | None:
        token = await super().__call__(request)
        if token:
            return token
        return request.cookies.get(self.token_key)
