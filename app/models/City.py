from datetime import datetime
from typing import List, Optional
from sqlmodel import Column, DateTime, Field, Relationship, SQLModel, String
from app.models.Address import Address


class City(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(sa_column=Column(String, nullable=False))
    code: str = Field(sa_column=Column(String, nullable=False))
    created_at: Optional[datetime] = Field(
        default=None, sa_column=Column(DateTime, default=datetime.utcnow)
    )
    updated_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow),
    )
    addresses: Optional[List["Address"]] = Relationship(back_populates="city")
