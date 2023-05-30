from utils.constants import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

if "sqlite" in config["DATABASE_URL"]:
    engine = create_engine(
        config["DATABASE_URL"], connect_args={"check_same_thread": False}
    )
else:
    engine = create_engine(config["DATABASE_URL"])

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """This is the function to get back a db instance.

    Yields:
        Session: SessionLocal a instance of Session from sqlalchemy.orm as a database instance
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
