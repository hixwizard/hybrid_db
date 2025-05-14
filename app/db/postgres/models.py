from sqlalchemy import Column, Integer, String, Text

from app.db.postgres.base import base as Base


class Book(Base):
    """Модель объекта книги."""
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, index=True)
    author = Column(String)
    description = Column(Text)
