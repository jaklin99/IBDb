from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.schemas import book as schemas
from app.models import book as models


def get_book_by_id(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()


def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Book).offset(skip).limit(limit).all()


def create_book(db: Session, book: schemas.Book):
    book_db = models.Book(**book.dict())
    db.add(book_db)
    db.commit()
    db.close()
    return f"Created book {book_db}"


def update_book(db: Session, book_id: int, book: schemas.Book):
    return None


def delete_book(db: Session, book_id: int, book: schemas.Book):
    book_db = db.query(models.Book).get(book_id)

    if book_db:
        db.delete(book_db)
        db.commit()
        db.close()

    return f"Deleted successfully!"
