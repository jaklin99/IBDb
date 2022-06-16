from fastapi import HTTPException
from typing import List
from fastapi import Header, APIRouter

from app.api.models import ReviewIn, ReviewOut, ReviewUpdate
from app.api import db_manager
from app.api.service import is_user_present, is_article_present

reviews = APIRouter()


@reviews.get('/', response_model=List[ReviewOut])
async def index():
    return await db_manager.get_all_articles()


@reviews.get('/{id}', response_model=ReviewOut)
async def get_review(id: int):
    review = await db_manager.get_review(id)
    if not review:
        raise HTTPException(status_code=404, detail="review not found")
    return review


@reviews.post('/', status_code=201)
async def create_review(payload: ReviewIn):
    userId = payload.userId
    articleId = payload.articleId

    if not is_user_present(userId):
        raise HTTPException(
            status_code=404, detail=f"User with id:{userId} not found")
    if not is_article_present(articleId):
        raise HTTPException(
            status_code=404, detail=f"Article with id:{articleId} not found")

    reviewId = await db_manager.add_review(payload)
    response = {
        'id': reviewId,
        **payload.dict()
    }

    return response


@reviews.put('/{id}')
async def update_review(id: int, payload: ReviewUpdate):
    review = await db_manager.get_review(id)
    if not review:
        raise HTTPException(status_code=404, detail="review not found")

    update_data = payload.dict(exclude_unset=True)

    review_in_db = ReviewIn(**review)

    updated_review = review_in_db.copy(update=update_data)

    return await db_manager.update_review(id, updated_review)


@reviews.delete('/{id}')
async def delete_review(id: int):
    review = await db_manager.get_review(id)
    if not review:
        raise HTTPException(status_code=404, detail="review not found")
    return await db_manager.delete_review(id)