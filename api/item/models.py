from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, TIMESTAMP

from api.database import Base
from api.category.models import category


class Item(Base):
    __tablename__ = "Item"

    item_id = Column(Integer, primary_key=True)
    item_name = Column(String, nullable=False)
    article = Column(String, unique=True, nullable=False)
    category_id = Column(Integer, ForeignKey(category.c.category_id))
    firm = Column(String, nullable=True)
    description = Column(String, nullable=False)
    price = Column(Numeric, nullable=False)
    amount = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), default=datetime.now())
    updated_at = Column(TIMESTAMP(timezone=True), nullable=True)


item = Item.__table__
