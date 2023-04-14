from datetime import datetime

from pydantic import BaseModel


class ItemCreate(BaseModel):
    item_id: int
    item_name: str
    article: str
    category_id: int
    firm: str
    description: str
    price: float
    amount: int
    created_at: datetime
    updated_at: datetime


class ItemRead(BaseModel):
    item_name: str
    article: str
    category_id: int
    firm: str
    description: str
    price: float
    amount: int

    class Config:
        orm_mode = True


class ItemUpdate(BaseModel):
    item_name: str
    article: str
    category_id: int
    firm: str
    description: str
    price: float
    amount: int
    updated_at: datetime
