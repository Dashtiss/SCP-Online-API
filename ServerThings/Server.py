from pydantic import BaseModel



class Server(BaseModel):
    ServerName: str | None = None
    ServerInfo: dict | None = None
