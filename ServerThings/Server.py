from pydantic import BaseModel


class Server(BaseModel):
    ServerName: str | None = None
    ServerID: int | None = None
