from datetime import datetime, timedelta, timezone
from models.schemas.jwt import Token, TokenData
from jose import jwt, JWTError
from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from dotenv import load_dotenv

import os

load_dotenv()

SECRET_KEY = os.getenv('SECRET')

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 15

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

def create_access_token(data = dict, expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
    


