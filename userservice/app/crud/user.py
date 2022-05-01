from sqlalchemy.orm import Session

from app.schemas import user as schemas
from app.models import user as models
from app.auth import utils


def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_user(db: Session, id: int):
    db_user = db.query(models.User).filter(models.User.id == id).first()
    return db_user


def create_user(username, email, password, db: Session):
    # hash the password - user.password
    hashed_password = utils.hash(password)
    password = hashed_password

    user_db = models.User(username=username, email=email, password=password)
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return f"Created book {user_db}"


def update_user(db: Session, id: int, username: str, email: str):
    db_user = get_user(db=db, id=id)
    db_user.username = username
    db_user.email = email

    db.commit()
    db.refresh(db_user)  # refresh the attribute of the given instance
    return db_user


def delete_user(db: Session, user: schemas.User):
    user_db = db.query(models.User).get(user.id)

    if user_db:
        db.delete(user_db)
        db.commit()
        db.close()

    return f"Deleted successfully!"
