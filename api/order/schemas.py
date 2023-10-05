from typing import Optional, List, Dict
from pydantic import BaseModel

from api.client.schemas import JsonClientCreate


class JsonOrderListCreate(BaseModel):
    id: int
    product: int
    order: int
    amount: int
    price: float

class JsonOrder(BaseModel):
    id: int
    total_price: float
    order_status: str
    payment_status: str
    delivery_address: str
    user: JsonClientCreate
    orderList: List[JsonOrderListCreate]


class OrderInfoCreate(BaseModel):
    order_id: int
    total_price: float
    client_id: int
    order_status: str
    payment_status: str
    delivery_address: str


class OrderInfoRead(BaseModel):
    order_id: int
    total_price: float
    client_id: int
    order_status: str
    payment_status: str
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
    amount: int
    price: float


class OrderListRead(BaseModel):
    item_id: int
    order_info_id: int
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
    amount: int
    price: float

    class Config:
        orm_mode = True
