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
@users.post('/', status_code=201)
async def add_user(username:str,email:str,password:str, db: Session = Depends(get_db)):
    new_user = crudUser.create_user(username=username,email=email,password=password, db=db)
    return new_user


# # UPDATE
# @users.put('/{id}', response_model=schemas.User)
# async def update_user(user_id: int, user: schemas.UserBase, db: Session = Depends(get_db)):
#     # get object from database
#     user_db = crudUser.get_user_by_id(db, user_id)
#     # check if the object exists
#     if not user_db:
#         raise HTTPException(status_code=404, detail=f"User with such id: {user_id} not found")
#     updated_user = crudUser.update_user(db, user_id, user)
#     return updated_user

@users.put("/{id}/") #id is a path parameter
def update_user(id:int, username:str, email:str, db:Session=Depends(get_db)):
    #get friend object from database
    db_friend = crudUser.get_user(db=db, id=id)
    #check if friend object exists
    if db_friend:
        updated_friend = crudUser.update_user(db=db, id=id, username=username, email=email)
        return updated_friend
    else:
        return {"error": f"User with id {id} does not exist"}


# DELETE
@users.delete('/{user_id}', status_code=204)
async def delete_book(user_id: int, db: Session = Depends(get_db)):
    user_db = crudUser.get_user_by_id(db, user_id)
    if not user_db:
        raise HTTPException(status_code=404, detail=f"User with such id: {user_id} not found")

    return crudUser.delete_user(db, user_db)

