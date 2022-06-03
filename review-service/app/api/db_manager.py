from app.api.models import ReviewIn, ReviewOut, ReviewUpdate
from app.api.db import reviews, database


async def add_review(payload: ReviewIn):
    query = reviews.insert().values(**payload.dict())

    return await database.execute(query=query)


async def get_all_books():
    query = reviews.select()
    return await database.fetch_all(query=query)


async def get_review(id):
    query = reviews.select(reviews.c.id == id)
    return await database.fetch_one(query=query)


async def update_review(id: int, payload: ReviewIn):
    query = (
        reviews
        .update()
        .where(reviews.c.id == id)
        .values(**payload.dict())
    )
    return await database.execute(query=query)


async def delete_review(id: int):
    query = reviews.delete().where(reviews.c.id == id)
    return await database.execute(query=query)