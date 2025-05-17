from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession as Session

from app.services.book import create_book, get_book, get_books
from app.models.schemas import BookCreate, Book
from app.db.postgres.session import get_db

router = APIRouter()


@router.post('/', response_model=Book)
async def create_new_book(book: BookCreate, db: Session = Depends(get_db)):
    """POST: Запись объекта книги."""
    return await create_book(db, book)


@router.get('/{id}', response_model=Book)
async def read_book(id: int, db: Session = Depends(get_db)):
    """GET_ID: Получение объекта книги по ID."""
    if (book := await get_book(db, id)) is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Книга не найдена.'
        )
    return book


@router.get('/', response_model=dict[str, list[Book]])
async def read_books(db: Session = Depends(get_db)):
    """GET_ALL: Получение всех объектов книг."""
    return {"books": await get_books(db)}
