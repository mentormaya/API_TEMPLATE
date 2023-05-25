from typing import Annotated
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from app.security.token import security

from app.database.config import get_db

user = APIRouter()


@user.get("/")
def get_users(
    token: Annotated[str, Depends(security)],
    db: Session = Depends(get_db),
):
    print(token)
    # # user = db.query(User).filter(User.id == user_id).first()
    # if user:
    #     return {"id": user.id, "name": user.name}
    return {"message": token}
