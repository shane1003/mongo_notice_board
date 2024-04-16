from app.config.config import collection_account
from app.services.security import verify_password
from fastapi import APIRouter, Depends, status, HTTPException, Response
from app.models.schemas.user import get_user_by_username

def authenticate_user(username: str, password: str):
    user = get_user_by_username(username)
    if not user:
        return False
    if not verify_password(password, user['password']):
        return False
    return user