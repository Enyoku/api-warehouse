from fastapi import APIRouter, Depends
from sqlalchemy import insert, select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from api.database import get_async_session
from api.client.models import client
from api.client.schemas import (ClientCreate, ClientRead,
                                ClientUpdate, ClientDelete)

client_router = APIRouter(tags=["Client"], prefix="/client")


@client_router.post("")
async def create_client(new_client: ClientCreate, session: AsyncSession = Depends(get_async_session)):
    query = insert(client).values(**new_client.dict())
    await session.execute(query)
    await session.commit()
    return {"status": "ok"}


@client_router.get("/{id}", response_model=List[ClientRead])
async def get_client_by_id(id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(client).where(client.c.client_id == id)
    result = await session.execute(query)
    await session.commit()
    return result.all()


@client_router.get("", response_model=List[ClientCreate])
async def get_all_clients(session: AsyncSession = Depends(get_async_session)):
    query = select(client)
    result = await session.execute(query)
    await session.commit()
    return result.fetchall()


@client_router.patch("/{id}")
async def update_client(id: int, updated_client: ClientUpdate, session: AsyncSession = Depends(get_async_session)):
    query = update(client).values(**updated_client.dict()).where(client.c.client_id == id)
    await session.execute(query)
    await session.commit()
    return {"status": "updated"}


@client_router.delete("/{id}")
async def update_client(id: int, session: AsyncSession = Depends(get_async_session)):
    query = delete(client).where(client.c.client_id == id)
    await session.execute(query)
    await session.commit()
    return {"status": "deleted"}
