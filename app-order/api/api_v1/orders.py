from typing import Optional

from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from core import settings
from core.db import db_core

from .schemas.order import (
    CreateOrderSchema,
    GetOrderSchema,
    GetOrdersSchema
)


# создание роутера для api пользователя, импорт настроек префикса и тегов
router = APIRouter(
    prefix=settings.api.v1.users,
    tags=settings.api.v1.tags
)


@router.get("/orders", response_model=GetOrdersSchema)
async def get_user(
    session: AsyncSession = Depends(db_core.session_getter),
    cancelled: Optional[bool] = None,
    limit: Optional[int] = None,
):
    # crud операции с аргументов session
    pass