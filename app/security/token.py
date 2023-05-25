from datetime import datetime, timedelta
from typing import Union, Any
from jose import jwt, JWTError
from fastapi import HTTPException
from utils.constants import config
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer

# JWT configuration
security = OAuth2PasswordBearer(tokenUrl="auth/token", scheme_name="JWT")

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

config["REFRESH_TOKEN_EXPIRE_DAYS"] = (
    config["REFRESH_TOKEN_EXPIRE_DAYS"] * 60 * 24  # converted to days
)


def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(
            minutes=config["ACCESS_TOKEN_EXPIRE_MINUTES"]
        )

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, config["JWT_SECRET_KEY"], config["ALGORITHM"])
    return encoded_jwt


def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(
            minutes=config["REFRESH_TOKEN_EXPIRE_DAYS"]
        )

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(
        to_encode, config["JWT_REFRESH_SECRET_KEY"], config["ALGORITHM"]
    )
    return encoded_jwt


def verify_token(token: str):
    try:
        payload = jwt.decode(
            token, config["JWT_SECRET_KEY"], algorithms=[config["ALGORITHM"]]
        )
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


def hash_password(password: str) -> str:
    return password_context.hash(password)


def verify_password(password: str, hashed_pass: str) -> bool:
    return password_context.verify(password, hashed_pass)
