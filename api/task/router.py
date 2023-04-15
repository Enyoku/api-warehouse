from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy import insert, select, delete, update
from sqlalchemy.ext.asyncio import AsyncSession

from api.database import get_async_session
from api.task.models import task
from api.task.schemas import TaskCreate, TaskRead, TaskUpdate


router = APIRouter(tags=["Task"], prefix="/task")


@router.post("")
async def create_task(new_task: TaskCreate, session: AsyncSession = Depends(get_async_session)):
    query = insert(task).values(**new_task.dict())
    await session.execute(query)
    await session.commit()
    return {"status": "created"}


@router.get("/{id}", response_model=List[TaskRead])
async def get_task_by_id(id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(task).where(task.c.task_id == id)
    result = await session.execute(query)
    await session.commit()
    return result.fetchall()


@router.get("", response_model=List[TaskRead])
async def get_all_task(session: AsyncSession = Depends(get_async_session)):
    query = select(task)
    result = await session.execute(query)
    await session.commit()
    return result.fetchall()


@router.patch("/{id}")
async def update_task(id: int, updated_task: TaskUpdate, session: AsyncSession = Depends(get_async_session)):
    query = update(task).values(**updated_task.dict()).where(task.c.task_id == id)
    await session.execute(query)
    await session.commit()
    return {"status": "updated"}


@router.delete("/{id}")
async def delete_task(id: int, session: AsyncSession = Depends(get_async_session)):
    query = delete(task).where(task.c.task_id == id)
    await session.execute(query)
    await session.commit()
    return {"status": "deleted"}
