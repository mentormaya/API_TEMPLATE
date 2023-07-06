from datetime import datetime
from typing import List, Optional
from sqlmodel import Column, DateTime, Field, Relationship, SQLModel, String
from app.models.City import City


class State(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(sa_column=Column(String, nullable=False))
    code: str = Field(sa_column=Column(String, nullable=False))
    capital: str = Field(sa_column=Column(String))
    created_at: Optional[datetime] = Field(
        default=None, sa_column=Column(DateTime, default=datetime.utcnow)
    )
    updated_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow),
    )
    cities: Optional[List["City"]] = Relationship(back_populates="city")
