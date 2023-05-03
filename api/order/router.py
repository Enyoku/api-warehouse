from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, select, update, delete

from api.database import get_async_session
from api.order.models import order_info, order_list
from api.item.models import item
from api.order.schemas import OrderInfoCreate, OrderInfoRead, OrderInfoUpdate
from api.order.schemas import OrderListCreate, OrderListRead, OrderListReadModified


order_info_router = APIRouter(tags=["OrderInfo"], prefix="/order_info")
order_list_router = APIRouter(tags=["OrderList"], prefix="/order_list")


@order_info_router.post("")
async def create_order_info(new_order: OrderInfoCreate, session: AsyncSession = Depends(get_async_session)):
    query = insert(order_info).values(**new_order.dict())
    await session.execute(query)
    await session.commit()
    return {"status": "created"}


@order_info_router.get("", response_model=List[OrderInfoRead])
async def get_all_order_info(sesion: AsyncSession = Depends(get_async_session)):
    query = select(order_info)
    result = await sesion.execute(query)
    await sesion.commit()
    return result.fetchall()


@order_info_router.get("{id}", response_model=List[OrderInfoRead])
async def get_order_info_by_id(id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(order_info).where(order_info.c.order_id == id)
    result = await session.execute(query)
    await session.commit()
    return result.fetchall()


@order_info_router.patch("{id}")
async def update_order_info(id: int, updated_order_info: OrderInfoUpdate, session: AsyncSession = Depends(get_async_session)):
    query = update(order_info).values(**updated_order_info.dict()).where(order_info.c.order_id == id)
    await session.execute(query)
    await session.commit()
    return {"status": "updated"}


@order_info_router.delete("{id}")
async def delete_order_info(id: int, session: AsyncSession = Depends(get_async_session)):
    query = delete(order_info).where(order_info.c.order_id == id)
    await session.execute(query)
    await session.commit()
    return {"status": "deleted"}

# ======================================================================================================================


@order_list_router.post("")
async def create_order_list(new_order: OrderListCreate, session: AsyncSession = Depends(get_async_session)):
    query = insert(order_list).values(**new_order.dict())
    await session.execute(query)
    await session.commit()
    return {"status": "created"}


@order_list_router.get("{id}", response_model=List[OrderListReadModified])
async def get_order_list_modified(id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(order_list.c.order_info_id, item.c.item_name, item.c.article, item.c.category_id, item.c.firm,
                   order_list.c.operation_code, order_list.c.amount, order_list.c.price).where(
        order_list.c.order_info_id == id).join_from(order_list, item, order_list.c.item_id == item.c.item_id)
    result = await session.execute(query)
    await session.commit()
    return result.fetchall()


@order_list_router.delete("{id}")
async def delete_order_list(id: int, session: AsyncSession = Depends(get_async_session)):
    query = delete(order_list).where(order_list.c.order_list_id == id)
    await session.execute(query)
    await session.commit()
    return {"status": "deleted"}
