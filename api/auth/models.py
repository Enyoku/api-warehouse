from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean
from fastapi_users.db import SQLAlchemyBaseUserTable

from api.database import Base


class Employee(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "Employee"

    id: int = Column(Integer, primary_key=True)
    username: str = Column(String(30), unique=True, nullable=False)
    full_name: str = Column(String(50), nullable=False)
    hashed_password: str = Column(String(length=1024), nullable=False)
    email: str = Column(String, nullable=False)
    position: str = Column(String, nullable=False)
    created_on: datetime = Column(DateTime, default=datetime.now())
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)
