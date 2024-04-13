from app.config.config import collection_account
from app.services.security import verify_password
from fastapi import APIRouter, Depends, status, HTTPException, Response


def authenticate_user(username: str, password: str):
    user = collection_account.find_one({"account_id" : username})
    if not user:
        return False
    if not verify_password(password, user.model_dump()['password']):
        return False
    return user.model_dump()