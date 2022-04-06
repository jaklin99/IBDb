from typing import List
from fastapi import APIRouter, HTTPException

from app.schemas import review

mock_db = [{
    'Content': 'Brave New World is ...',
    'Book': 'Brave New World',
    'User': 'Jane',

}]

# registered a new API route using the APIRouter from FastAPI
r_api_router = APIRouter(
    prefix="/reviews"
)


# GET
@r_api_router.get('/', response_model=List[review.Review])
async def get_review():
    return mock_db


# POST
# payload - the info received from/sent to the server
@r_api_router.post('/', status_code=201)
async def add_review(payload: review.Review):
    book = payload.dict()
    mock_db.append(book)
    return {'id': len(mock_db) - 1}


@r_api_router.delete('/{id}')
async def delete_review(id: int):
    books_len = len(mock_db)
    if 0 <= id <= books_len:
        del mock_db[id]
        return None
    raise HTTPException(status_code=404, detail="Book with given id not found")
