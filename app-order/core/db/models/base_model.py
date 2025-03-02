from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import declared_attr

from core import settings
from utils import camel_case_to_snake_case



class Base(DeclarativeBase):
    """Класс для наследования в ORM модели"""

    # добавление уникальных значений для всех уникальных и др. значений при инициализации моделей и миграции
    metadata = MetaData( 
        naming_convention=settings.database.naming_conventions
    )

    @declared_attr.directive
    def __tablename__(cls) -> str:
        """Генерация имени для каждой ORM модели на основе их класс-имени"""
        return f"{camel_case_to_snake_case(cls.__name__)}s"
