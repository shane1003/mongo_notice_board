from fastapi import APIRouter, status
from models.schemas.user import UserInCreate, user_input_2_db
from config.config import collection_account
from services.security import get_password_hash

router = APIRouter()

back_ups = [UserInCreate(username="test1", password1="test1", password2="test1", nickname="test1"),
            UserInCreate(username="test2", password1="test2", password2="test2", nickname="test2")]

@router.post("/", status_code=status.HTTP_201_CREATED)
async def register():

    return()

@router.post("/backup", status_code=status.HTTP_201_CREATED)
async def account_back_up():
    for i, create in enumerate(back_ups):
        input = user_input_2_db(create)
        collection_account.insert_one(input)