from typing import Optional

from pydantic import BaseModel


class JsonClientCreate(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str

    class Config:
        orm_mode = True


class ClientCreate(BaseModel):
    client_id: int
    full_name: str
    email: str
    address: str

    class Config:
        orm_mode = True


class ClientRead(BaseModel):
    full_name: str
    email: str
    address: str

    class Config:
        orm_mode = True


class ClientUpdate(BaseModel):
    full_name: Optional[str]
    email: Optional[str]
    address: Optional[str]


class ClientDelete(BaseModel):
    client_id: int
