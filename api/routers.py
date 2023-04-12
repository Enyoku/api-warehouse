from fastapi import APIRouter

from api.auth.router import auth_router
from api.task.router import router as task_router


routers = APIRouter()

routers.include_router(task_router)
routers.include_router(auth_router)

