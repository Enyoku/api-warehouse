from sqlalchemy import Column, Integer, String

from api.database import Base


class Category(Base):
    __tablename__ = "Category"

    category_id = Column(Integer, primary_key=True)
    category_name = Column(String, unique=True)


category = Category.__table__
