from typing import List, Optional
from pydantic import BaseModel

class User(BaseModel):
    username : str
    nickname : str
    articles : List[int]

class UserInDB(User):
    hashed_password : str