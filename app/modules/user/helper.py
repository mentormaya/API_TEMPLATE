from datetime import datetime
from typing import Any, Union
from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from pydantic import ValidationError
from app.database.config import get_db
from app.modules.user import models
from app.modules.user.schemas import SystemUser, TokenPayload
from app.security import token
from utils.constants import config
from sqlalchemy.orm import Session


async def get_current_user(
    token: str = Depends(token.security), db: Session = Depends(get_db)
) -> SystemUser:
    try:
        payload = jwt.decode(
            token, config["JWT_SECRET_KEY"], algorithms=[config["ALGORITHM"]]
        )
        token_data = TokenPayload(**payload)

        if datetime.fromtimestamp(token_data.exp) < datetime.now():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except (JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user: Union[dict[str, Any], None] = (
        db.query(models.User).filter(models.User.email == token_data.sub).first()
    )

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find user",
        )

    return user.__dict__
