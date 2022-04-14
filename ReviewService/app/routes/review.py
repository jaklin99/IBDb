from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
<<<<<<< HEAD
from app.schemas import review as schemas
=======
from app.schemas import review
>>>>>>> 65c530dc3ff53bccb3ee14a8f4b31d4238c52a47
from app.crud import review as crudReview
from app.database import engine, get_db

# registered a new API route using the APIRouter from FastAPI
r_router = APIRouter(
    prefix="/reviews"
)


# GET
<<<<<<< HEAD
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
=======
@r_router.get('/', response_model=List[review.ReviewBase])
async def get_all_reviews(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    reviews_db = crudReview.get_reviews(db, skip=skip, limit=limit)
    return reviews_db


@r_router.get('/{id}', response_model=List[review.Review])
async def get_review_by_id(r_id: int, db: Session = Depends(get_db)):
    review_db = crudReview.get_review_by_id(db, r_id)
    if not review_db:
        raise HTTPException(status_code=404, detail=f"Book with such id: {book_id} not found")

    return review_db
>>>>>>> 65c530dc3ff53bccb3ee14a8f4b31d4238c52a47


# POST
# payload - the info received from/sent to the server
<<<<<<< HEAD
@r_router.post('/', status_code=201, response_model=schemas.Review)
async def add_review(review_: schemas.ReviewCreate, db: Session = Depends(get_db)):
    return crudReview.create_review(db, review_)
=======
@r_router.post('/', status_code=201, response_model=review.ReviewCreate)
async def add_review(review: review.ReviewCreate, db: Session = Depends(get_db)):
    return crudReview.create_book(db, review)
>>>>>>> 65c530dc3ff53bccb3ee14a8f4b31d4238c52a47


# UPDATE
@r_router.put('/{id}')
async def update_review():
    return crudReview.update_review()


# DELETE
@r_router.delete('/{id}')
async def delete_review():
    return crudReview.delete_review()