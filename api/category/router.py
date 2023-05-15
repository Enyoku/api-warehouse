from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy import insert, select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from api.database import get_async_session
from api.auth.base_config import current_verified_user
from .models import category
from .schemas import CategoryCreate, CategoryRead

category_router = APIRouter(tags=["Category"], prefix="/category")


@category_router.post("")
async def create_category(new_category: CategoryCreate, session: AsyncSession = Depends(get_async_session),
                          current_user=Depends(current_verified_user)):
    query = insert(category).values(**new_category.dict())
    await session.execute(query)
    await session.commit()
    return {"status": "ok"}


@category_router.get("", response_model=List[CategoryRead])
async def get_all_categories(session: AsyncSession = Depends(get_async_session),
                          current_user=Depends(current_verified_user)):
    query = select(category)
    result = await session.execute(query)
    await session.commit()
    return result.fetchall()


@category_router.delete("/{id}")
async def delete_category(id: int, current_user=Depends(current_verified_user)
                          , session: AsyncSession = Depends(get_async_session)):
    query = delete(category).where(category.c.category_id == id)
    await session.execute(query)
    await session.commit()
    return {"status": "deleted"}
