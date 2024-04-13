from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

from bson import ObjectId
from typing import Annotated

from app.models.domain.user import User
from app.services.jwt import Token
from app.models.schemas.user import get_one_account
from config.config import collection_account

router = APIRouter()

@router.get("/{id}")
async def get_account_by_id(id: str):
    account_Info = get_one_account(collection_account.find_one({"_id" : ObjectId(id)}))
    return account_Info

@router.put("/{id}/userModify")
async def get_account_by_id(id: str):
    account_Info = get_one_account(collection_account.find_one({"_id": ObjectId(id)}))
    return account_Info
'''
@router.post("/login")
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
'''