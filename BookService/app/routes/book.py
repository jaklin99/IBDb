from typing import List
from fastapi import APIRouter, HTTPException

from app.schemas import book

mock_db = [{
    'name': 'Brave New World',
    'plot': 'A new innovative world with no touch to the natural habitat of humans',
    'genres': ['Fiction'],
    'author': 'Aldous Huxley',
    'year': 1932
}]

# registered a new API route using the APIRouter from FastAPI
books = APIRouter(
    prefix="/books"
)


# GET
@books.get('/', response_model=List[book.Book])
async def index():
    return mock_db


# POST
# payload - the info received from/sent to the server
@books.post('/', status_code=201)
async def add_book(payload: book.Book):
    book = payload.dict()
    mock_db.append(book)
    return {'id': len(mock_db) - 1}


# UPDATE
@books.put('/{id}')
async def update_book(id: int, payload: book.Book):
    book = payload.dict()
    books_len = len(mock_db)
    # check if the list is empty
    if 0 <= id <= books_len:
        # id is the index of the mock db
        mock_db[id] = book
        return None
    raise HTTPException(status_code=404, detail="Book with given id not found")


@books.delete('/{id}')
async def delete_book(id: int):
    books_len = len(mock_db)
    if 0 <= id <= books_len:
        del mock_db[id]
        return None
    raise HTTPException(status_code=404, detail="Book with given id not found")
