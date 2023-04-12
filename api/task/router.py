from fastapi import APIRouter

from api.config import DB_PASS

router = APIRouter(tags=["Task"], prefix="/task")


@router.get('/')
def ping():
    return {'status': DB_PASS}
