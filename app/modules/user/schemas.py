from typing import List
from uuid import UUID
from pydantic import BaseModel, Field, EmailStr


class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str
    type: str


class TokenPayload(BaseModel):
    sub: str = None
    exp: int = None


class UserBase(BaseModel):
    email: EmailStr = Field(..., description="User Email")


class UserAuth(UserBase):
    password: str = Field(..., description="User Password")


class UserCreate(UserAuth):
    name: str = Field(..., description="User Full Name")


class User(UserBase):
    name: str = Field(..., description="User Full Name")
    id: int


class SystemUser(User):
    password: str = Field(..., description="User Password")


class UsersList(BaseModel):
    users: List[User]
