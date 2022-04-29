from typing import List
from fastapi import APIRouter
from sqlalchemy.orm import Session
from app.database import engine, get_db
from app.crud import user as crudUser
from app.schemas import user as schemas
from fastapi import Depends, HTTPException


# registered a new API route using the APIRouter from FastAPI
users = APIRouter(
    prefix="/users",
    tags=['Users']
)


# GET
@users.get('/', response_model=List[schemas.User])
async def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    user_db = crudUser.get_users(db, skip=skip, limit=limit)
    return user_db


@users.get("/{id}", response_model=schemas.User)
async def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user_db = crudUser.get_user_by_id(db, user_id)
    if not user_db:
        raise HTTPException(status_code=404, detail=f"User with such id: {user_id} not found")

    return user_db


# POST
@users.post('/', status_code=201, response_model=schemas.User)
async def add_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crudUser.create_user(user, db)


# UPDATE
@users.put('/{id}')
async def update_user():
    return crudUser.update_user()

# DELETE
@users.delete('/{user_id}', status_code=204)
async def delete_book(user_id: int, db: Session = Depends(get_db)):
    user_db = crudUser.get_user_by_id(db, user_id)
    if not user_db:
        raise HTTPException(status_code=404, detail=f"Book with such id: {user_id} not found")

    return crudUser.delete_user(db, user_db)

