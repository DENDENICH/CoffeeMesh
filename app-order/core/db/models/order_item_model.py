import uuid
from datetime import datetime, timezone

from sqlalchemy import (
    Integer,
    String,
    ForeignKey,
    DateTime
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .annotateds import intpk
from ..base_model import Base


def generate_datetime_now_utc():
    return datetime.now(timezone.utc)


class OrderItemModel(Base):
    """ORM модель объекта заказа"""

    id: Mapped[intpk]
    items = relationship('OrderItemModel', backref='order')
    status: Mapped[str] = mapped_column(
        String,
        nullable=False,
        default='created'
    )
    created: Mapped[datetime] = mapped_column(
        DateTime,
        default=generate_datetime_now_utc
    )
    # schedule_id: Mapped[str] = mapped_column(
    #     String,
    #     primary_key=True,
    #     default=generate_uuid
    # )
    # delivery_id: Mapped[str] = mapped_column(
    #     String,
    #     primary_key=True,
    #     default=generate_uuid
    # )
    