from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from app.database.config import get_db

user = APIRouter()


@user.get("/")
def get_users(db: Session = Depends(get_db)):
    # # user = db.query(User).filter(User.id == user_id).first()
    # if user:
    #     return {"id": user.id, "name": user.name}
    return {"message": "User not found"}
