<<<<<<< HEAD
from typing import List, Optional

from pydantic import BaseModel
from pydantic.schema import date
=======
from typing import List

from pydantic import BaseModel
from pydantic.schema import datetime
>>>>>>> 65c530dc3ff53bccb3ee14a8f4b31d4238c52a47


class ReviewBase(BaseModel):
    content: str
<<<<<<< HEAD
    # book: str
    # user: str
    # books_id: List[int]
    date: date
=======
    book: str
    user: str
    date_time: datetime
>>>>>>> 65c530dc3ff53bccb3ee14a8f4b31d4238c52a47

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    id: int
    # user_id: int
    class Config:  #used to provide configurations to Pydantic
<<<<<<< HEAD
        orm_mode = True

=======
        orm_mode = True
>>>>>>> 65c530dc3ff53bccb3ee14a8f4b31d4238c52a47
