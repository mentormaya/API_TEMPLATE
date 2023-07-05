from datetime import datetime
from typing import List, Optional
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlmodel import SQLModel, Field, Relationship


class Country(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(sa_column=Column(String, nullable=False))
    code: str = Field(sa_column=Column(String, nullable=False))
    capital: str = Field(sa_column=Column(String, nullable=False))
    created_at: Optional[datetime] = Field(
        default=None, sa_column=Column(DateTime, default=datetime.utcnow)
    )
    updated_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow),
    )
    states: Optional[List["State"]] = Relationship(back_populates="country")


class State(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(sa_column=Column(String, nullable=False))
    code: str = Field(sa_column=Column(String, nullable=False))
    capital: str = Field(sa_column=Column(String, nullable=False))
    created_at: Optional[datetime] = Field(
        default=None, sa_column=Column(DateTime, default=datetime.utcnow)
    )
    updated_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow),
    )
    cities: Optional[List["City"]] = Relationship(back_populates="city")


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
    person: Optional[List["Person"]] = Relationship(back_populates="address")


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
