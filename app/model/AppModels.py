from datetime import datetime
from typing import List, Optional
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlmodel import SQLModel, Field, Relationship


class Country(SQLModel, table=True):
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
    addresses: Optional[List["Address"]] = Relationship(back_populates="country")


class State(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(sa_column=Column(String, nullable=False))
    created_at: Optional[datetime] = Field(
        default=None, sa_column=Column(DateTime, default=datetime.utcnow)
    )
    updated_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow),
    )


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


class Address(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    street: str = Field(sa_column=Column(String, nullable=False))
    postal_code: str = Field(sa_column=Column(String, nullable=False))
    city_id: int = Field(sa_column=Column(Integer, ForeignKey("city.id")))
    state_id: int = Field(sa_column=Column(Integer, ForeignKey("state.id")))
    country_id: int = Field(sa_column=Column(Integer, ForeignKey("country.id")))
    created_at: Optional[datetime] = Field(
        default=None, sa_column=Column(DateTime, default=datetime.utcnow)
    )
    updated_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow),
    )
    person: Optional["Person"] = Relationship(back_populates="address")
    city: Optional["City"] = Relationship(back_populates="addresses")
    state: Optional[State] = Relationship(back_populates="addresses")
    country: Optional["Country"] = Relationship(back_populates="addresses")


class Person(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str = Field(sa_column=Column(String, nullable=False))
    last_name: str = Field(sa_column=Column(String, nullable=False))
    address_id: int = Field(sa_column=Column(Integer, ForeignKey("address.id")))
    created_at: Optional[datetime] = Field(
        default=None, sa_column=Column(DateTime, default=datetime.utcnow)
    )
    updated_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow),
    )
    address: Optional[Address] = Relationship(back_populates="person")


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
    users: List["User"] = Relationship(back_populates="role")


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(sa_column=Column(String, unique=True, nullable=False))
    password: str = Field(sa_column=Column(String, nullable=False))
    role_id: Optional[int] = Field(sa_column=Column(Integer, nullable=False))
    is_active: bool = Field(sa_column=Column(Boolean, default=True))
    person_id: Optional[int] = Field(sa_column=Column(Integer, nullable=False))
    created_at: Optional[datetime] = Field(
        default=None, sa_column=Column(DateTime, default=datetime.utcnow)
    )
    updated_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow),
    )
    role: Optional["Role"] = Relationship(back_populates="users")
    person: Optional["Person"] = Relationship(back_populates="users")
