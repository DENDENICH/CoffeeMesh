from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    """Базовая модель пользователя"""
    username: str


class UserCreate(UserBase):
    """Модель регистрации и создания пользователя"""
    pass


class UserRead(UserBase):

    # По умолчанию уже есть, используется для совместимости с объектом БД
    model_config = ConfigDict(
        from_attributes=True
    )

    id: int 
