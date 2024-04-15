from bson import ObjectId
from pydantic import BaseModel, validator, constr
from typing import Optional, List
from models.domain.user import User, UserInDB
from services.security import get_password_hash

class UserInCreate(BaseModel):
    username : str
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

def get_one_user(account) -> dict:
    return{
        "id": str(account.get("_id")),
        "username": account.get("username"),
        "nickname": account.get("nickname"),
        "articles": account.get("articles")
    }

def get_user_by_username(collection_account, username: str) -> dict:
    if username in collection_account:
        user_dict = collection_account['username']
        return UserInDB(**user_dict)
    
def user_input_2_db(input: UserInCreate):
    return{
        "username": input["username"],
        "password": get_password_hash(input["password1"]),
        "nickname": input["nickname"],
        "articles": []
    }

#class UserInLogin()