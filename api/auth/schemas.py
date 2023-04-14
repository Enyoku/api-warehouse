from typing import Optional
from datetime import datetime

from fastapi_users import schemas
from pydantic import BaseModel


class UserRead(schemas.BaseUser[int]):
    id: int
    full_name: str
    email: str
    username: str
    position: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    username: str
    full_name: str
    email: str
    password: str
    position: str
    created_on: datetime
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False


class UserUpdate(schemas.BaseUserUpdate):
    username: Optional[str]
    full_name: Optional[str]
    position: Optional[str]
    password: Optional[str]
    email: Optional[str]
    is_active: Optional[bool]
    is_superuser: Optional[bool]
    is_verified: Optional[bool]


class Ver(BaseModel):
    is_verified: bool
