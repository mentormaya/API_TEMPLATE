from typing import Annotated
from uuid import uuid4
from fastapi import Depends, APIRouter, HTTPException, Request, status
from sqlalchemy.orm import Session
from app.modules.user.helper import get_current_user
from app.modules.user.schemas import SystemUser, UserAuth, UserOut

from app.security import token
from app.database.config import get_db
from utils.logger import Logger

user = APIRouter()

logger = Logger()


@user.get("/", summary="Get a list of all users")
def get_users(
    req: Request,
    user_token: Annotated[str, Depends(token.security)],
    db: Session = Depends(get_db),
):
    logger.log("All users fetched!", host=req.client.host)
    print(user_token)
    # # user = db.query(User).filter(User.id == user_id).first()
    # if user:
    #     return {"id": user.id, "name": user.name}
    return {"message": user_token}


@user.post("/", summary="Create new user", response_model=UserOut)
async def create_user(
    data: UserAuth,
    req: Request,
    user_token: Annotated[str, Depends(token.security)],
    db: Session = Depends(get_db),
):
    # querying database to check if user already exist
    user = db.get(data.email, None)
    if user is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exist",
        )
    user = {
        "email": data.email,
        "password": token.hash_password(data.password),
        "id": str(uuid4()),
    }
    db[data.email] = user  # saving user to database
    return user


@user.get(
    "/me", summary="Get details of currently logged in user", response_model=UserOut
)
async def get_me(user: SystemUser = Depends(get_current_user)):
    return user
