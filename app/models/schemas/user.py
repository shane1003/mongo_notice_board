from bson import ObjectId
from pydantic import BaseModel, validator
from typing import Optional, List
from models.domain.user import User

def get_one_account(account) -> dict:
    return{
        "id" : str(account.get("_id")),
        "username" : account.get("username"),
        "password" : account.get("password"),
        "nickname" : account.get("nickname"),
        "articles" : account.get("articles")
    }

#class UserInLogin()

class UserInCreate(BaseModel):
    user_id : str
    password1 : str
    password2 : str
    nickname : str
    
    @validator('username', 'password1', 'password2', 'nickname')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('Please fill in all the spaces')
        return v
    
    @validator('password2')
    def password_match(cls, v, values):
        if 'password1' in values and v != values['password2']:
            raise ValueError('Password does not match')
        return v

class UserInUpdate(BaseModel):
    password : Optional[str] = None
    nickname : Optional[str] = None

class UserWithToken(User):
    token: str