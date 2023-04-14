from typing import List, Any

from fastapi import APIRouter, Depends
from sqlalchemy import insert, select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from api.item.models import item
from api.item.schemas import ItemCreate, ItemRead, ItemUpdate
from api.database import get_async_session

item_router = APIRouter(tags=["Item"], prefix="/item")


@item_router.post("")
async def create_item(new_item: ItemCreate, session: AsyncSession = Depends(get_async_session)):
    query = insert(item).values(**new_item.dict())
    await session.execute(query)
    await session.commit()
    return {"status": "created"}


@item_router.get("/{id}", response_model=List[ItemRead])
async def get_item_by_id(id: int, session: AsyncSession = Depends(get_async_session)) -> Any:
    query = select(item).where(item.c.item_id == id)
    result = await session.execute(query)
    await session.commit()
    return result.fetchall()


@item_router.patch("/{id}")
async def update_item(id: int, updated_item: ItemUpdate, session: AsyncSession = Depends(get_async_session)) -> Any:
    query = update(item).values(**updated_item.dict()).where(item.c.item_id == id)
    await session.execute(query)
    await session.commit()
    return {"status": "updated"}


@item_router.delete("/{id}")
async def delete_item(id: int, session: AsyncSession = Depends(get_async_session)) -> Any:
    query = delete(item).where(item.c.item_id == id)
    await session.execute(query)
    await session.commit()
    return {"status": "deleted"}
