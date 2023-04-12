from fastapi import APIRouter, Depends

from api.auth.schemas import UserRead, UserCreate
from api.auth.base_config import auth_backend, fastapi_users, current_user

auth_router = APIRouter(tags=["Auth"], prefix="/auth")
auth_router.include_router(fastapi_users.get_auth_router(auth_backend))
auth_router.include_router(fastapi_users.get_register_router(UserRead, UserCreate))
auth_router.include_router(fastapi_users.get_verify_router(UserRead))


@auth_router.get("/ping")
async def test(user=Depends(current_user)):
    return {"status": "ok"}
