from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class ReviewIn(BaseModel):
    content: str
    userId: int
    # created: datetime = datetime.now()
    bookId: int


class ReviewOut(ReviewIn):
    id: int


class ReviewUpdate(ReviewIn):
    content: Optional[str] = None
    # modified: Optional[datetime] = None