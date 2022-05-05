from pydantic import BaseModel
from typing import List, Optional

class BookIn(BaseModel):
    name: str
    plot: str
    genres: List[str]
    users_id: List[int]


class BookOut(BookIn):
    id: int


class BookUpdate(BookIn):
    name: Optional[str] = None
    plot: Optional[str] = None
    genres: Optional[List[str]] = None
    users_id: Optional[List[int]] = None