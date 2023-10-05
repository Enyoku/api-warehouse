from sqlalchemy import Column, ForeignKey, Integer, String, Numeric
from sqlalchemy.orm import relationship

from api.database import Base
from api.client.models import client
from api.item.models import item


class OrderInfo(Base):
    __tablename__ = "OrderInfo"

    order_id = Column(Integer, primary_key=True)
    total_price = Column(Numeric, nullable=False)
    client_id = Column(Integer, ForeignKey(client.c.client_id))
    order_status = Column(String, nullable=False)
    payment_status = Column(String, nullable=False)
    delivery_address = Column(String, nullable=False)


order_info = OrderInfo.__table__


class OrderList(Base):
    __tablename__ = "OrderList"

    order_list_id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey(item.c.item_id))
    order_info_id = Column(Integer, ForeignKey(order_info.c.order_id))
    amount = Column(Integer, nullable=False)
    price = Column(Numeric, nullable=False)


order_list = OrderList.__table__
