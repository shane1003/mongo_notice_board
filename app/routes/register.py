from fastapi import APIRouter, status
from app.models.domain.user import User, UserInDB
from app.config.config import collection_account
from app.services.security import get_password_hash

router = APIRouter()

back_up = [{"username": "test1", "password": get_password_hash("test1"), "nickname": "test1", "articles": []},
           {"username": "test2", "password": get_password_hash("test2"), "nickname": "test2", "articles": []}]

@router.post("/", status_code=status.HTTP_201_CREATED)
async def register():

    return()

@router.post("/backup", status_code=status.HTTP_201_CREATED)
async def account_back_up():
    for data in back_up:
        collection_account.insert_one(data)