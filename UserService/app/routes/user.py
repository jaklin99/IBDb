from typing import List
from fastapi import APIRouter, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from app.schemas.user import User, UserInDB
from fastapi import Depends

# from app.services.user import get_current_active_user, get_current_user, fake_hash_password

mock_db = [{
    'name': 'John',

}]
fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}


# registered a new API route using the APIRouter from FastAPI
users = APIRouter(
    prefix="/users"
)


# GET
@users.get('/', response_model=List[User])
async def index():
    return mock_db


# @users.get("/users/me")
# async def read_users_me(current_user: User = Depends(get_current_user)):
#     return current_user
#
#
# @users.get("/users/me")
# async def read_users_me(current_user: User = Depends(get_current_active_user)):
#     return current_user
#
#
# # POST
# # payload - the info received from/sent to the server
# @users.post('/', status_code=201)
# async def add_user(payload: User):
#     user = payload.dict()
#     mock_db.append(user)
#     return {'id': len(mock_db) - 1}
#
#
# @users.post("/token")
# async def login(form_data: OAuth2PasswordRequestForm = Depends()):
#     user_dict = fake_users_db.get(form_data.username)
#     if not user_dict:
#         raise HTTPException(status_code=400, detail="Incorrect username or password")
#     user = UserInDB(**user_dict)
#     hashed_password = fake_hash_password(form_data.password)
#     if not hashed_password == user.hashed_password:
#         raise HTTPException(status_code=400, detail="Incorrect username or password")
#
#     return {"access_token": user.username, "token_type": "bearer"}


# UPDATE
@users.put('/{id}')
async def update_user(id: int, payload: User):
    user = payload.dict()
    users_len = len(mock_db)
    # check if the list is empty
    if 0 <= id <= users_len:
        # id is the index of the mock db
        mock_db[id] = user
        return None
    raise HTTPException(status_code=404, detail="Book with given id not found")


@users.delete('/{id}')
async def delete_user(id: int):
    users_len = len(mock_db)
    if 0 <= id <= users_len:
        del mock_db[id]
        return None
    raise HTTPException(status_code=404, detail="Book with given id not found")
