from pydantic import BaseModel, validator, constr
from app.models.domain.user import UserInDB, User
from app.services.security import get_password_hash
from app.config.config import collection_account

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
        if 'password1' in values and v != values['password1']:
            raise ValueError('Password does not match')
        return v

def get_one_user(account) -> dict:
    return{
        "id": str(account.get("_id")),
        "username": account.get("username"),
        "nickname": account.get("nickname"),
        "articles": account.get("articles")
    }

def get_user_by_username(username: str) -> dict:
    user = collection_account.find_one({"username" : username})
    if user:
        return user

#class UserInLogin()