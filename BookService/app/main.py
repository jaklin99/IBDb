from fastapi import FastAPI

from app import database as db
from app.routes import book as book_routes
from app.models import book

# book.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(book_routes.books)


#
# @app.on_event("startup")
# async def startup():
#     await db.connect()
#
#
# @app.on_event("shutdown")
# async def shutdown():
#     await db.disconnect()