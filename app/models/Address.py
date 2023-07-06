from datetime import datetime
from typing import List, Optional

# from app.models.Person import Person
from sqlmodel import (
    Column,
    DateTime,
    Field,
    ForeignKey,
    Integer,
    Relationship,
    SQLModel,
    String,
)


class Address(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    street: str = Field(sa_column=Column(String, nullable=False))
    postal_code: str = Field(sa_column=Column(String, nullable=False))
    city_id: int = Field(sa_column=Column(Integer, ForeignKey("city.id")))
    state_id: int = Field(sa_column=Column(Integer, ForeignKey("state.id")))
    country_id: int = Field(sa_column=Column(Integer, ForeignKey("country.id")))
    created_at: Optional[datetime] = Field(
        sa_column=Column(DateTime, default=datetime.utcnow)
    )
    updated_at: Optional[datetime] = Field(
        sa_column=Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    )
    city: Optional["City"] = Relationship(back_populates="address")
    state: Optional["State"] = Relationship(back_populates="address")
    country: Optional["Country"] = Relationship(back_populates="address")
    person: Optional[List["Person"]] = Relationship(back_populates="address")
