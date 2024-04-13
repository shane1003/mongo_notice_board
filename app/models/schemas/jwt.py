from datetime import datetime as dt

from pydantic import BaseModel

class JWTMeta(BaseModel):
    exp: dt
    sub: str

class JWTUser(BaseModel):
    id : str