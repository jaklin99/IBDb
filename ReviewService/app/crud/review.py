from sqlalchemy.orm import Session

from app.schemas import review as schemas
from app.models import review as models


def get_review_by_id(db: Session, r_id: int):
    return db.query(models.Review).filter(models.Review.id == r_id).first()


def get_reviews(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Review).offset(skip).limit(limit).all()


def create_book(db: Session, review: schemas.Review):
    review_db = models.Review(**review.dict())
    db.add(review_db)
    db.commit()
    db.close()
    return f"Posted review {review_db}"


def update_review():
    return None


def delete_review(db: Session, r_id: int, review: schemas.Review):
    review_db = db.query(models.Review).get(r_id)

    if review_db:
        db.delete(review_db)
        db.commit()
        db.close()

    return f"Deleted successfully!"

