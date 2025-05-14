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


# TODO: сделать get_book_or_404
async def get_book(db: AsyncSession, id: int):
    """Получение объекта книги."""
    return await db.get(BookModel, id)
