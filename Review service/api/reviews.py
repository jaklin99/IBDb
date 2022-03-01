from typing import List
from fastapi import APIRouter, HTTPException

from schemas import Review

mock_db = [{
    'content': 'Brave New World'

}]

# registered a new API route using the APIRouter from FastAPI
reviews = APIRouter()


# GET
@reviews.get('/reviews', response_model=List[Review])
async def index():
    return mock_db


# POST
# payload - the info received from/sent to the server
@reviews.post('/add', status_code=201)
async def add_book(payload: Review):
    book = payload.dict()
    mock_db.append(book)
    return {'id': len(mock_db) - 1}


# UPDATE
@reviews.put('/{id}')
async def update_book(id: int, payload: Review):
    review = payload.dict()
    reviews_len = len(mock_db)
    # check if the list is empty
    if 0 <= id <= reviews_len:
        # id is the index of the mock db
        mock_db[id] = review
        return None
    raise HTTPException(status_code=404, detail="Book with given id not found")


@reviews.delete('/{id}')
async def delete_movie(id: int):
    reviews_len = len(mock_db)
    if 0 <= id <= reviews_len:
        del mock_db[id]
        return None
    raise HTTPException(status_code=404, detail="Book with given id not found")
