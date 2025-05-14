from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession as Session

from app.services.book import create_book, get_book
from app.models.schemas import BookCreate, Book
from app.db.postgres.session import get_db

router = APIRouter()


@router.post('/', response_model=Book)
async def create_new_book(book: BookCreate, db: Session = Depends(get_db)):
    """Запись объекта книги."""
    return await create_book(db, book)


@router.get('/{id}', response_model=Book)
async def read_book(id: int, db: Session = Depends(get_db)):
    """Получение объекта книги по ID."""
    return await get_book(db, id)
