from fastapi_users.authentication import CookieTransport, JWTStrategy
from fastapi_users.authentication import AuthenticationBackend
from fastapi_users import FastAPIUsers

from api.auth.models import Employee
from api.auth.manager import get_user_manager
from api.config import SECRET

cookie = CookieTransport(cookie_name="warehouse", cookie_max_age=3600, cookie_samesite="none")


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[Employee, int](
    get_user_manager,
    [auth_backend]
)

current_user = fastapi_users.current_user()
current_verified_user = fastapi_users.current_user(verified=True)
