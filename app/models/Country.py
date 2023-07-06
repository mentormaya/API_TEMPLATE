from datetime import datetime
from typing import List, Optional
from fastapi import Depends
from sqlmodel import Column, DateTime, Field, Relationship, SQLModel, Session, String

from app.database.config import get_db
from app.models.State import State
from app.models.CountrySeed import countries


class Country(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(sa_column=Column(String, nullable=False))
    nicename: str = Field(sa_column=Column(String))
    capital: str = Field(sa_column=Column(String))
    iso: str = Field(sa_column=Column(String))
    iso3: Optional[str] = Field(sa_column=Column(String))
    numcode: Optional[int] = Field(sa_column=Column(String))
    phonecode: int = Field(sa_column=Column(String))
    created_at: Optional[datetime] = Field(
        default=None, sa_column=Column(DateTime, default=datetime.utcnow)
    )
    updated_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow),
    )
    states: Optional[List["State"]] = Relationship(back_populates="country")


def seed_countries(db: Session = Depends(get_db)):
    for country_data in countries:
        country = Country(
            id=country_data[0],
            iso=country_data[1],
            name=country_data[2],
            nicename=country_data[3],
            iso3=country_data[4],
            numcode=country_data[5],
            phonecode=country_data[6],
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )
        db.add(country)
    db.commit()


seed_countries()
