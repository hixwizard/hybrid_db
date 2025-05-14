from pydantic import BaseModel


class BookBase(BaseModel):
    """Базовая схема для книги."""
    title: str
    author: str
    description: str


class BookCreate(BookBase):
    """Схема создания."""
    pass


class Book(BookBase):
    """Схема с конфигурацией ORM."""
    id: int

    class Config:
        from_attributes = True
