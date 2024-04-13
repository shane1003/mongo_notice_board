from datetime import datetime, timedelta
from typing import Dict

from jose import jwt
from pydantic import ValidationError, BaseModel

from app.models.domain.user import User
from app.models.schemas.jwt import JWTMeta, JWTUser
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from passlib.context import CryptContext

import os

load_dotenv()

SECRET = os.getenv('SECRET')


JWT_SUBJECT = "access"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None