from sqlalchemy.orm import Session

from app.schemas import review as schemas
from app.models import review as models



def get_review(db: Session, user_id: int):
    return db.query(models.Book).filter(models.Book.id == user_id).first()


def get_review_by_id(db: Session, email: str):
    return db.query(models.Book).filter(models.Book.email == email).first()


def get_reviews(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Book).offset(skip).limit(limit).all()

#
# def create_book(db: Session, user: schemas.BookCreate):
#     fake_hashed_password = user.password + "notreallyhashed"
#     db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

