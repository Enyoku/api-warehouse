from typing import Optional

from pydantic import BaseModel, Field


class TaskCreate(BaseModel):
    task_id: int
    manager_id: int
    storekeeper_id: Optional[int]
    order_info_id: int
    task_status: str


class TaskRead(BaseModel):
    task_id: int
    manager_id: int
    storekeeper_id: Optional[int]
    order_info_id: int
    task_status: str

    class Config:
        orm_mode = True


class TaskUpdate(BaseModel):
    storekeeper_id: Optional[int]
    task_status: str
