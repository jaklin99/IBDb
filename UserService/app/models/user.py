from app.database import Base
from typing import Optional
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
import sqlalchemy as sa


class User(Base):
    __tablename__ = "User"
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    username = sa.Column(sa.String(256), nullable=True)
    password = sa.Column(sa.String, index=True, nullable=False)
    email = sa.Column(sa.String, index=True, nullable=False)

    # book_id = sa.Column(sa.Integer, foregn_key="users.id")
    # book = relationship("User", back_populates="books") and books must be created as a relationship in User

