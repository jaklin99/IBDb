<<<<<<< HEAD
from typing import Optional, List
=======
from typing import Optional
>>>>>>> 65c530dc3ff53bccb3ee14a8f4b31d4238c52a47

from pydantic import (
    BaseModel,
    EmailStr,
    SecretStr,
    validator,
    root_validator
)
<<<<<<< HEAD
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
=======
>>>>>>> 65c530dc3ff53bccb3ee14a8f4b31d4238c52a47


class UserBase(BaseModel):
    username: str
    password: str
<<<<<<< HEAD
    email: EmailStr


class UserInDB(UserBase):
    hashed_password: str

=======
    email: Optional[str] = None
>>>>>>> 65c530dc3ff53bccb3ee14a8f4b31d4238c52a47

class UserCreate(UserBase):
    pass

<<<<<<< HEAD
class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserIn(UserBase):
    password: str


=======
>>>>>>> 65c530dc3ff53bccb3ee14a8f4b31d4238c52a47
class User(UserBase):
    id: int

    # book_id: int
    class Config:  # used to provide configurations to Pydantic
        orm_mode = True
