from typing import Optional
from datetime import datetime

from fastapi_users import schemas


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
    pass
