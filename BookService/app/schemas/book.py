from typing import List

from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
<<<<<<< HEAD
    # genre: List[str]
    # author: str
    # year: int

=======
    genre: List[str]
    author: str
    year: int
>>>>>>> 65c530dc3ff53bccb3ee14a8f4b31d4238c52a47

class BookCreate(BookBase):
    pass

<<<<<<< HEAD

class Book(BookBase):
    id: int

    # user_id: int

    class Config:  # used to provide configurations to Pydantic
        orm_mode = True
=======
class Book(BookBase):
    id: int
    # user_id: int
    class Config:  #used to provide configurations to Pydantic
        orm_mode = True
>>>>>>> 65c530dc3ff53bccb3ee14a8f4b31d4238c52a47
