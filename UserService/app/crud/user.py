from sqlalchemy.orm import Session

from app.schemas import user as schemas
from app.models import user as models



def get_book(db: Session, user_id: int):
    return db.query(models.Book).filter(models.Book.id == user_id).first()


def get_book_by_id(db: Session, email: str):
    return db.query(models.Book).filter(models.Book.email == email).first()


def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Book).offset(skip).limit(limit).all()
