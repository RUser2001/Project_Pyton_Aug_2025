from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from . import token as token_util  # alias pt. modulul token.py

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token_str: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return token_util.verify_token(token_str, credentials_exception)

