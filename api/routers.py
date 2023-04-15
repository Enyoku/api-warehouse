from fastapi import APIRouter

from api.auth.router import auth_router, user_router
from api.task.router import router as task_router
from api.category.router import category_router
from api.client.router import client_router
from api.item.router import item_router
from api.order.router import order_info_router
from api.order.router import order_list_router


routers = APIRouter()

routers.include_router(task_router)
routers.include_router(auth_router)
routers.include_router(user_router)
routers.include_router(category_router)
routers.include_router(client_router)
routers.include_router(item_router)
routers.include_router(order_info_router)
routers.include_router(order_list_router)
