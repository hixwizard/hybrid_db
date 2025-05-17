from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.postgres.models import Book as BookModel
from app.models.schemas import BookCreate


async def create_book(db: AsyncSession, book: BookCreate):
    """Создание объекта по схеме BookCreate."""
    db_book = BookModel(**book.model_dump())
    db.add(db_book)
    await db.commit()
    await db.refresh(db_book)
    return db_book


async def get_book(db: AsyncSession, id: int):
    """Получение объекта книги."""
    return await db.get(BookModel, id)


async def get_books(db: AsyncSession):
    """Получение всех объектов книг."""
    res = await db.execute(select(BookModel))
    return res.scalars().all()
