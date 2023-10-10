from typing import List, Any

from fastapi import APIRouter, Depends
from sqlalchemy import insert, select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from api.item.models import item
from api.category.models import category
from api.item.schemas import ItemCreate, ItemRead, ItemUpdate, ItemReadModified, ItemCreateJson, ItemUpdateJson
from api.database import get_async_session

item_router = APIRouter(tags=["Item"], prefix="/item")


@item_router.post("")
async def create_item(new_item: ItemCreate, session: AsyncSession = Depends(get_async_session)):
    query = insert(item).values(**new_item.dict())
    await session.execute(query)
    await session.commit()
    return {"status": "created"}


@item_router.post("/create")
async def create_item_by_json(new_item: ItemCreateJson, session: AsyncSession = Depends(get_async_session)):
    query = insert(item).values(
        item_id=new_item.id,
        item_name=new_item.name,
        article=new_item.article,
        category_id=new_item.category,
        firm=new_item.firm,
        description=new_item.description,
        price=new_item.price,
        amount=new_item.amount,
        created_at=new_item.created_at,
        updated_at=new_item.updated_at,
    )
    await session.execute(query)
    await session.commit()
    return {"status": "created"}


@item_router.get("", response_model=List[ItemRead])
async def get_all_items(session: AsyncSession = Depends(get_async_session)):
    query = select(item)
    result = await session.execute(query)
    await session.commit()
    return result.fetchall()


@item_router.get("/{id}", response_model=List[ItemReadModified])
async def get_item_modified(id: int, session: AsyncSession = Depends(get_async_session)) -> Any:
    query = select(item.c.item_name, item.c.article,
                   category.c.category_name, item.c.firm, item.c.description, item.c.price, item.c.amount)\
        .where(item.c.item_id == id).join_from(item, category, item.c.category_id == category.c.category_id)
    result = await session.execute(query)
    await session.commit()
    return result.fetchall()


@item_router.patch("/{id}")
async def update_item(id: int, updated_item: ItemUpdate, session: AsyncSession = Depends(get_async_session)) -> Any:
    query = update(item).values(**updated_item.dict()).where(item.c.item_id == id)
    await session.execute(query)
    await session.commit()
    return {"status": "updated"}


@item_router.patch("/{id}/update")
async def update_item_by_json(id: int, updated_item: ItemUpdateJson, session: AsyncSession = Depends(get_async_session)):
    query = update(item).values(
        item_name=updated_item.name,
        article=updated_item.article,
        category_id=updated_item.category,
        firm=updated_item.firm,
        description=updated_item.description,
        price=updated_item.price,
        amount=updated_item.amount,
        updated_at=updated_item.updated_at,
    ).where(item.c.item_id == id)
    await session.execute(query)
    await session.commit()
    return {"status": "updated"}


@item_router.delete("/{id}")
async def delete_item(id: int, session: AsyncSession = Depends(get_async_session)) -> Any:
    query = delete(item).where(item.c.item_id == id)
    await session.execute(query)
    await session.commit()
    return {"status": "deleted"}
