from sqlalchemy import Column, ForeignKey, Integer, String

from api.database import Base
from api.auth.models import empl
from api.order.models import order_info


class Task(Base):
    __tablename__ = "Task"

    task_id = Column(Integer, primary_key=True)
    manager_id = Column(Integer, ForeignKey(empl.c.id), nullable=False)
    storekeeper_id = Column(Integer, ForeignKey(empl.c.id), nullable=True)
    order_info_id = Column(Integer, ForeignKey(order_info.c.order_id), nullable=False)
    task_status = Column(String, nullable=False)


task = Task.__table__
