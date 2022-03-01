from typing import List
from fastapi import APIRouter, HTTPException

from schemas import User

mock_db = [{
    'name': 'John',

}]

# registered a new API route using the APIRouter from FastAPI
users = APIRouter()


# GET
@users.get('/users', response_model=List[User])
async def index():
    return mock_db


# POST
# payload - the info received from/sent to the server
@users.post('/add', status_code=201)
async def add_book(payload: User):
    user = payload.dict()
    mock_db.append(user)
    return {'id': len(mock_db) - 1}


# UPDATE
@users.put('/{id}')
async def update_book(id: int, payload: User):
    user = payload.dict()
    users_len = len(mock_db)
    # check if the list is empty
    if 0 <= id <= users_len:
        # id is the index of the mock db
        mock_db[id] = user
        return None
    raise HTTPException(status_code=404, detail="Book with given id not found")


@users.delete('/{id}')
async def delete_movie(id: int):
    users_len = len(mock_db)
    if 0 <= id <= users_len:
        del mock_db[id]
        return None
    raise HTTPException(status_code=404, detail="Book with given id not found")
