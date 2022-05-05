from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import BookIn, BookOut, BookUpdate
from app.api import db_manager
from app.api.service import is_user_present

books = APIRouter()

@books.post('/', response_model=BookOut, status_code=201)
async def create_book(payload: BookIn):
    for user_id in payload.users_id:
        if not is_user_present(user_id):
            raise HTTPException(status_code=404, detail=f"Cast with given id:{user_id} not found")

    book_id = await db_manager.add_book(payload)
    response = {
        'id': book_id,
        **payload.dict()
    }

    return response

@books.get('/', response_model=List[BookOut])
async def get_books():
    return await db_manager.get_all_books()

@books.get('/{id}/', response_model=BookOut)
async def get_book(id: int):
    book = await db_manager.get_book(id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@books.put('/{id}/', response_model=BookOut)
async def update_book(id: int, payload: BookUpdate):
    book = await db_manager.get_book(id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    update_data = payload.dict(exclude_unset=True)

    if 'users_id' in update_data:
        for user_id in payload.users_id:
            if not is_user_present(user_id):
                raise HTTPException(status_code=404, detail=f"User with given id:{user_id} not found")

    book_in_db = BookIn(**book)

    updated_book = book_in_db.copy(update=update_data)

    return await db_manager.update_book(id, updated_book)

@books.delete('/{id}/', response_model=None)
async def delete_book(id: int):
    book = await db_manager.get_book(id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return await db_manager.delete_book(id)