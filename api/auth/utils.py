from fastapi import Depends
from fastapi.responses import JSONResponse
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from api.database import get_async_session
from api.auth.models import Employee


def generate_cookie(token: str):
    content = {"token": f"{token}"}
    response = JSONResponse(content=content)
    response.set_cookie(key="fakesession", value="fake-cookie-session-value")
    return response


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, Employee)
