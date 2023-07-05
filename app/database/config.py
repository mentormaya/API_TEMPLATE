from utils.constants import config
from sqlmodel import Session, create_engine

if "sqlite" in config["DATABASE_URL"]:
    engine = create_engine(
        config["DATABASE_URL"], connect_args={"check_same_thread": False}
    )
else:
    engine = create_engine(config["DATABASE_URL"])


def get_db():
    """This is the function to get back a db instance.

    Yields:
        Session: SessionLocal a instance of Session from sqlalchemy.orm as a database instance
    """
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()
