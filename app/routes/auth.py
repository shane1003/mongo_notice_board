from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from datetime import timedelta
from app.services.jwt import ACCESS_TOKEN_EXPIRE_MINUTES
from app.models.schemas.jwt import Token
from app.services.auth import authenticate_user
from app.services.jwt import create_access_token

router = APIRouter(tags=['Authentication'])

@router.post('/login')
def login(user_credentials: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:

    user = authenticate_user(user_credentials.username, user_credentials.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Incorrect username or password",
            headers={"WWW-Authentication": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    #create token
    access_token = create_access_token(
        data = {"user_id": user['username']}, expires_delta=access_token_expires
    )
    return {"access_token" : access_token, "token_type": "bearer"}