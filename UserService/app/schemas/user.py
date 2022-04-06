from typing import Optional

from pydantic import (
    BaseModel,
    EmailStr,
    SecretStr,
    validator,
    root_validator
)


class UserBase(BaseModel):
    username: str
    password: str
    email: Optional[str] = None

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    # book_id: int
    class Config:  # used to provide configurations to Pydantic
        orm_mode = True
