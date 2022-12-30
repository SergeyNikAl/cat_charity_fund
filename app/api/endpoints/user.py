from http import HTTPStatus

from fastapi import APIRouter, HTTPException

from app.core.user import auth_backend, fastapi_users
from app.schemas.user import UserCreate, UserRead, UserUpdate

FORBIDDEN_DELETE_USER_MESSAGE = 'Удаление пользователей запрещено!'

router = APIRouter()

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix='/auth/jwt',
    tags=['Авторизация']
)

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix='/auth',
    tags=['Авторизация']
)

router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix='/users',
    tags=['Пользователи']
)


@router.delete(
    '/users/{id}',
    tags=['Пользователи'],
    deprecated=True
)
def delete_user(id: str):
    """Удаление пользователя недоступно"""

    raise HTTPException(
        status_code=HTTPStatus.METHOD_NOT_ALLOWED,
        detail=FORBIDDEN_DELETE_USER_MESSAGE
    )
