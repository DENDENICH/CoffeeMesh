from typing import Optional, List

from enum import Enum

from uuid import UUID
from datetime import datetime

from pydantic import BaseModel
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


class CerateOrderSchema(BaseModel):
    order: List[OrderItemSchema]


class GetOrderSchema(BaseModel):
    id: UUID
    created: datetime
    status: Status
    order: List[OrderItemSchema]


class GetOrdersSchema(BaseModel):
    order: List[GetOrderSchema]
    