from typing import List
import asyncio

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, select, update, delete, exists

from api.database import get_async_session
from api.client.models import client
from api.order.models import order_info, order_list, OrderInfo
from api.item.models import item
from api.order.schemas import OrderInfoCreate, OrderInfoRead, OrderInfoUpdate, JsonOrder
from api.order.schemas import OrderListCreate, OrderListRead, OrderListReadModified


order_info_router = APIRouter(tags=["OrderInfo"], prefix="/order_info")
order_list_router = APIRouter(tags=["OrderList"], prefix="/order_list")


@order_info_router.post("")
async def create_order_info(new_order: OrderInfoCreate, session: AsyncSession = Depends(get_async_session)):
    query = insert(order_info).values(**new_order.dict())
    await session.execute(query)
    await session.commit()
    return {"status": "created"}


@order_info_router.post("/create")
async def create_order_by_json(json: JsonOrder, session: AsyncSession = Depends(get_async_session)):
    order_exists = await session.scalars(select(order_info).filter(order_info.c.order_id == json.id))
    client_exists = await session.scalars(select(client).where(client.c.client_id == json.user.id))

    # Checking for an existing order
    if not bool(order_exists.first()):
        # Checking for an existing client
        if not bool(client_exists.first()):
            client_query = insert(client).values(
                client_id=json.user.id,
                full_name=json.user.first_name + " " + json.user.last_name,
                email=json.user.email,
                address=json.delivery_address
            )
            await session.execute(client_query)
            await session.commit()
        else:
            order_info_query = insert(order_info).values(
                order_id=json.id,
                total_price=json.total_price,
                client_id=json.user.id,
                order_status=json.order_status,
                payment_status=json.payment_status,
                delivery_address=json.delivery_address
            )
            await session.execute(order_info_query)
            await session.commit()

            for product in json.orderList:
                order_list_query = insert(order_list).values(
                    order_list_id=product.id,
                    item_id=product.product,
                    order_info_id=product.order,
                    amount=product.amount,
                    price=product.price,
                )
                await session.execute(order_list_query)
                await session.commit()
            return {"status": "created"}
    else:
        return JSONResponse({"error": "Order with this id already exists"}, status_code=400)


@order_info_router.get("", response_model=List[OrderInfoRead])
async def get_all_order_info(sesion: AsyncSession = Depends(get_async_session)):
    query = select(order_info)
    result = await sesion.execute(query)
    await sesion.commit()
    return result.fetchall()


@order_info_router.get("/{id}", response_model=List[OrderInfoRead])
async def get_order_info_by_id(id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(order_info).where(order_info.c.order_id == id)
    result = await session.execute(query)
    await session.commit()
    return result.fetchall()


@order_info_router.patch("/{id}")
async def update_order_info(id: int, updated_order_info: OrderInfoUpdate, session: AsyncSession = Depends(get_async_session)):
    query = update(order_info).values(**updated_order_info.dict()).where(order_info.c.order_id == id)
    await session.execute(query)
    await session.commit()
    return {"status": "updated"}


@order_info_router.delete("/{id}")
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


@order_list_router.get("/{id}", response_model=List[OrderListReadModified])
async def get_order_list_modified(id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(order_list.c.order_list_id, order_list.c.order_info_id, item.c.item_id, item.c.item_name,
                   item.c.article, item.c.category_id,
                   item.c.firm, order_list.c.amount, 
                   order_list.c.price).where(
        order_list.c.order_info_id == id).join_from(order_list, item, order_list.c.item_id == item.c.item_id)
    result = await session.execute(query)
    await session.commit()
    return result.fetchall()


@order_list_router.delete("/{id}")
async def delete_order_list(id: int, session: AsyncSession = Depends(get_async_session)):
    query = delete(order_list).where(order_list.c.order_list_id == id)
    await session.execute(query)
    await session.commit()
    return {"status": "deleted"}
