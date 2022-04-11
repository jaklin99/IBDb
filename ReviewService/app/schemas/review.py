from typing import List, Optional

from pydantic import BaseModel
from pydantic.schema import date


class ReviewBase(BaseModel):
    content: str
    # book: str
    # user: str
    # books_id: List[int]
    date: date

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    id: int
    # user_id: int
    class Config:  #used to provide configurations to Pydantic
        orm_mode = True

