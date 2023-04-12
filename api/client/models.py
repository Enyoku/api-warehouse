from sqlalchemy import Column, Integer, String

from api.database import Base


class Client(Base):
    __tablename__ = "Client"

    client_id = Column(Integer, primary_key=True)
    full_name = Column(String(length=50), nullable=False)
    email = Column(String(length=50), nullable=False)
    address = Column(String(length=50), nullable=False)
