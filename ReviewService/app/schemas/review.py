from typing import List

from pydantic import BaseModel
from pydantic.schema import datetime


class ReviewBase(BaseModel):
    content: str
    book: str
    user: str
    date_time: datetime

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    id: int
    # user_id: int
    class Config:  #used to provide configurations to Pydantic
        orm_mode = True