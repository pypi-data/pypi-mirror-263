import time

from pydantic import BaseModel, Field


def epoch():
    return int(time.time())


class User(BaseModel):
    username: str
    password: str | None = None
    timestamp: int = Field(default_factory = epoch)

    def __str__(self) -> str:
        return f"{self.username}/{self.password}"
