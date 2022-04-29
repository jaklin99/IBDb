from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.schemas import book as schemas
from app.models import book as models


def get_book_by_id(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()


def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Book).offset(skip).limit(limit).all()


def get_book(db: Session, id: int):
    db_book = db.query(models.Book).filter(models.Book.id == id).first()
    return db_book


def create_book(db: Session, title: str, genre: str, author: str, year: int):
    book_db = models.Book(title=title, genre=genre, author=author, year=year)
    db.add(book_db)
    db.commit()
    db.refresh(book_db)
    return f"Created book {book_db}"


def update_book(db: Session, book_id: int, title: str, genre: str, author: str, year: int):
    db_book = get_book(db=db, id=book_id)

    db_book.title = title
    db_book.genre = genre
    db_book.author = author
    db_book.year = year

    db.commit()
    db.refresh(db_book)
    return db_book


def delete_book(db: Session, book: schemas.Book):
    book_db = db.query(models.Book).get(book.id)

    if book_db:
        db.delete(book_db)
        db.commit()
        db.close()

    return f"Deleted successfully!"
