from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session


from app.database.config import get_db

auth = APIRouter()


@auth.post("/token")
def get_token_by_login(db: Session = Depends(get_db)):
    return {"message": "Login successfull!"}
