from fastapi import APIRouter, Depends

from sqlalchemy import update, select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from api.auth.models import empl
from api.database import get_async_session
from api.auth.schemas import Ver

from api.auth.schemas import UserRead, UserCreate, UserUpdate
from api.auth.base_config import auth_backend, fastapi_users, current_user

auth_router = APIRouter(tags=["Auth"], prefix="/auth")
auth_router.include_router(fastapi_users.get_auth_router(auth_backend))
auth_router.include_router(fastapi_users.get_register_router(UserRead, UserCreate))
auth_router.include_router(fastapi_users.get_verify_router(UserRead))

user_router = APIRouter(tags=["User"], prefix="/user")
user_router.include_router(fastapi_users.get_users_router(UserRead, UserUpdate))


@auth_router.get("/ping")
async def test(user=Depends(current_user)):
    return {"status": "ok"}


@auth_router.post("/fake-verification")
async def test(id: int, ver: Ver, session: AsyncSession = Depends(get_async_session)):
    query = update(empl).values(**ver.dict()).where(empl.c.id == id)
    await session.execute(query)
    await session.commit()
    return {"status": "ok"}
