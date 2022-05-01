from typing import Optional, List

from pydantic import (
    BaseModel,
    EmailStr,
    SecretStr,
    validator,
    root_validator
)
from fastapi.security import (
    OAuth2PasswordBearer,
    OAuth2PasswordRequestForm,
    SecurityScopes,
)

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
    scopes: List[str] = []


class UserBase(BaseModel):
    username: str
    password: str
    email: EmailStr


class UserInDB(UserBase):
    hashed_password: str


class UserCreate(UserBase):
    pass

# class UserLogin(BaseModel):
#     email: EmailStr
#     password: str
#
# class UserIn(UserBase):
#     password: str


class User(UserBase):
    id: int

    # book_id: int
    class Config:  # used to provide configurations to Pydantic
        orm_mode = True
