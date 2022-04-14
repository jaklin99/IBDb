from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas import review as schemas
from app.crud import review as crudReview
from app.database import engine, get_db

# registered a new API route using the APIRouter from FastAPI
r_router = APIRouter(
    prefix="/reviews"
)


# GET
@r_router.get('/', response_model=List[schemas.Review])
async def get_all_reviews(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    r_db = crudReview.get_reviews(db, skip=skip, limit=limit)
    return r_db


@r_router.get('/{id}', response_model=List[schemas.Review])
async def get_review_by_id(r_id: int, db: Session = Depends(get_db)):
    r_db = crudReview.get_review_by_id(db, r_id)
    if not r_db:
        raise HTTPException(status_code=404, detail=f"Book with such id: {r_id} not found")

    return r_db


# POST
# payload - the info received from/sent to the server
@r_router.post('/', status_code=201, response_model=schemas.Review)
async def add_review(review_: schemas.ReviewCreate, db: Session = Depends(get_db)):
    return crudReview.create_review(db, review_)


# UPDATE
@r_router.put('/{id}')
async def update_review():
    return crudReview.update_review()


# DELETE
@r_router.delete('/{id}')
async def delete_review():
    return crudReview.delete_review()