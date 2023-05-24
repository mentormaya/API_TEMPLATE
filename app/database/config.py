from utils.constants import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

if "sqlite:///" in config["DATABASE_URL"]:
    engine = create_engine(
        config["DATABASE_URL"], connect_args={"check_same_thread": False}
    )
else:
    engine = create_engine(config["DATABASE_URL"])

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
