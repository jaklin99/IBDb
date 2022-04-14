from sqlalchemy.orm import Session

from app.schemas import user as schemas
from app.models import user as models
<<<<<<< HEAD
from app.auth import utils


def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(user: schemas.UserCreate, db: Session):
    # hash the password - user.password
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    user_db = models.User(**user.dict())
    db.add(user_db)
    db.commit()
    db.close()
    return f"Created book {user_db}"


def update_user(db: Session, user_id: int, user: schemas.User):
    return None


def delete_user(db: Session, user: schemas.User):
    user_db = db.query(models.User).get(user.id)

    if user_db:
        db.delete(user_db)
        db.commit()
        db.close()

    return f"Deleted successfully!"
=======



def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_id(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()
>>>>>>> 65c530dc3ff53bccb3ee14a8f4b31d4238c52a47
