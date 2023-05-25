from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from app.database.config import get_db

auth = APIRouter()


@auth.get("/login")
def login(db: Session = Depends(get_db)):
    return {"message": "Login successfull!"}
