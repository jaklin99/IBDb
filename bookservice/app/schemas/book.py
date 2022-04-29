from typing import List

from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    genre: str
    author: str
    year: int


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int

    # user_id: int

    class Config:  # used to provide configurations to Pydantic
        orm_mode = True
