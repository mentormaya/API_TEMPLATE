from typing import Annotated, List
from uuid import uuid4
from fastapi import Depends, APIRouter, HTTPException, Request, status
from sqlalchemy.orm import Session
from app.modules.user.helper import get_current_user
from app.modules.user.schemas import SystemUser, User, UserCreate
from app.modules.user import models
from app.security import token
from app.database.config import get_db
from app.security.token import hash_password
from utils.logger import Logger

user = APIRouter()

logger = Logger()


@user.get("/", summary="Get a list of all users", response_model=List[User])
def get_users(
    req: Request,
    user_token: Annotated[str, Depends(token.security)],
    db: Session = Depends(get_db),
):
    logger.log("All users fetched!", host=req.client.host)
    users = db.query(models.User).all()
    if not users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No User Information Found!",
        )
    users = [user.__dict__ for user in users]
    return users


@user.post("/", summary="Create new user", response_model=User)
async def create_user(
    user_data: UserCreate,
    req: Request,
    db: Session = Depends(get_db),
):
    # querying database to check if user already exist
    user = db.query(models.User).filter(models.User.email == user_data.email).first()
    if user is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exist",
        )
    user = models.User(
        name=user_data.name,
        email=user_data.email,
        password=hash_password(user_data.password),
    )
    db.add(user)
    db.commit()  # saving user to database
    db.refresh(user)
    return user.__dict__


@user.get("/me", summary="Get details of currently logged in user", response_model=User)
async def get_me(user: User = Depends(get_current_user)):
    return user
