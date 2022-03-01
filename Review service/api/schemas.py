from typing import List
from pydantic import BaseModel

class Review(BaseModel):
    content: str
