from api import Base
from typing import Optional
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
import sqlalchemy as sa


class User(Base):
    __tablename__ = "User"
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    username = sa.Column(sa.String(256), nullable=True)
    surname = sa.Column(sa.String(256), nullable=True)
    email = sa.Column(sa.String, index=True, nullable=False)


