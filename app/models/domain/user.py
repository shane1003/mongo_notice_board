from typing import List
from pydantic import BaseModel

class User(BaseModel):
    username : str
    password : str
    nickname : str
    articles = List[int]

class UserInDB(User):
    hashed_password : str

    def check_password(self, password: str) -> bool:
        return password == self.password
    
    def change_password(self, password: str) -> None:
        self.password = password