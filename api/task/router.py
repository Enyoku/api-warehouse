from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy import insert, select, delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.dialects import postgresql

from api.database import get_async_session
from api.task.models import task
from api.auth.models import empl
from api.task.schemas import TaskCreate, TaskRead, TaskUpdate, TaskReadModified


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


@router.get("", response_model=List[TaskReadModified])
async def get_all_task(session: AsyncSession = Depends(get_async_session)):
    empl1 = empl.alias("a")
    empl2 = empl.alias("b")
    query = select(task.c.task_id, task.c.manager_id, task.c.storekeeper_id, empl1.c.full_name.label("manager_name"),
                   empl2.c.full_name.label("storekeeper_name"), task.c.order_info_id,
                    task.c.task_status)\
        .join(empl1, task.c.manager_id == empl1.c.id, isouter=True).join(empl2, task.c.storekeeper_id == empl2.c.id, isouter=True)
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
