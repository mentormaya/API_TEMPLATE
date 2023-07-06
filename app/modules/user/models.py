from datetime import datetime
from typing import List, Optional
from sqlmodel import (
    Boolean,
    Column,
    DateTime,
    Integer,
    SQLModel,
    Field,
    Relationship,
    String,
)
from app.models.Person import Person


class Role(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(sa_column=Column(String, unique=True, nullable=False))
    created_at: Optional[datetime] = Field(
        default=None, sa_column=Column(DateTime, default=datetime.utcnow)
    )
    updated_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow),
    )
    users: Optional[List["User"]] = Relationship(back_populates="role")


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(sa_column=Column(String, unique=True, nullable=False))
    password: str = Field(sa_column=Column(String, nullable=False))
    email: str = Field(sa_column=Column(String, unique=True))
    active: bool = Field(sa_column=Column(Boolean, default=True))
    role_id: Optional[int] = Field(sa_column=Column(Integer, nullable=False))
    person_id: Optional[int] = Field(sa_column=Column(Integer, nullable=False))
    created_at: Optional[datetime] = Field(
        default=None, sa_column=Column(DateTime, default=datetime.utcnow)
    )
    updated_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow),
    )
    role: Optional["Role"] = Relationship(back_populates="user")
    person: Optional["Person"] = Relationship(back_populates="user")


# Insert/Seed Default User for testing purpose
