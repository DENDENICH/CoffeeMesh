from typing import Optional, List

from enum import Enum

from uuid import UUID
from datetime import datetime

from pydantic import BaseModel, Extra
from pydantic import conlist, conint


class Size(str, Enum):
    small = "small"
    medium = "medium"
    big = "big"


class Status(str, Enum):
    created = "created"
    progress = "progress"
    cancelled = "cancelled"
    dispatched = "dispatched"
    delivered = "delivered"


class OrderItemSchema(BaseModel):
    """Модель представления объекта заказа"""
    product: str
    size: Size
    quantity: Optional[int] = 1

    class Config:
        extra = "allow"


class CreateOrderSchema(BaseModel):
    """Модель представления объекта создание заказа"""
    order: List[OrderItemSchema]

    class Config:
        extra = "allow"


class GetOrderSchema(BaseModel):
    """Модель представления объекта отправки заказа"""
    id: UUID
    created: datetime
    status: Status
    order: List[OrderItemSchema]


class GetOrdersSchema(BaseModel):
    """Модель представления объекта отправки заказов"""
    order: List[GetOrderSchema]
    