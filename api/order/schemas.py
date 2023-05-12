from typing import Optional
from pydantic import BaseModel


class OrderInfoCreate(BaseModel):
    order_id: int
    total_price: float
    client_id: int
    operation_code: str
    delivery_address: str


class OrderInfoRead(BaseModel):
    order_id: int
    total_price: float
    client_id: int
    operation_code: str
    delivery_address: str

    class Config:
        orm_mode = True


class OrderInfoUpdate(BaseModel):
    total_price: float
    delivery_address: str


class OrderListCreate(BaseModel):
    order_list_id: int
    item_id: int
    order_info_id: int
    operation_code: str
    amount: int
    price: float


class OrderListRead(BaseModel):
    item_id: int
    order_info_id: int
    operation_code: str
    amount: int
    price: float

    class Config:
        orm_mode = True


class OrderListReadModified(BaseModel):
    order_list_id: int
    order_info_id: int
    item_id: int
    item_name: str
    article: str
    category_id: int
    firm: str
    operation_code: str
    amount: int
    price: float

    class Config:
        orm_mode = True
