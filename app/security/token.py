from utils.constants import config
from fastapi import HTTPException
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer

# JWT configuration
security = OAuth2PasswordBearer(tokenUrl="auth/token")


def verify_token(token: str):
    try:
        payload = jwt.decode(
            token, config["SECRET_KEY"], algorithms=[config["ALGORITHM"]]
        )
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
