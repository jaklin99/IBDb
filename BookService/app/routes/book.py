from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.crud import book as crudBook
from app.database.database import engine, get_db
from app.models.book import Book as bookModel
from app.schemas import book as schemas

# registered a new API route using the APIRouter from FastAPI
books = APIRouter(
    prefix="/books"
)


# GET
@books.get('/', response_model=List[schemas.Book])
async def get_all_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    books_db = crudBook.get_books(db, skip=skip, limit=limit)
    return books_db


@books.get('/{book_id}', response_model=schemas.Book)
async def get_book_by_id(book_id: int, db: Session = Depends(get_db)):
    book_db = crudBook.get_book_by_id(db, book_id)
    if not book_db:
        raise HTTPException(status_code=404, detail=f"Book with such id: {book_id} not found")

    return book_db


# POST
# payload - the info received from/sent to the server
@books.post('/', status_code=201, response_model=schemas.Book)
async def add_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crudBook.create_book(db, book)


# UPDATE
@books.put('/{book_id}', response_model=schemas.Book)
async def update_book(book_id: int, book: schemas.Book, db: Session = Depends(get_db)):
    book_db = crudBook.get_book_by_id(db, book_id)
    if not book_db:
        raise HTTPException(status_code=404, detail=f"Book with such id: {book_id} not found")

    return crudBook.update_book(db,book_id, book)


# DELETE
@books.delete('/{book_id}', status_code=204)
async def delete_book(book_id: int, db: Session = Depends(get_db)):
    book_db = crudBook.get_book_by_id(db, book_id)
    if not book_db:
        raise HTTPException(status_code=404, detail=f"Book with such id: {book_id} not found")

    return crudBook.delete_book(db, book_db)
