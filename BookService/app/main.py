from fastapi import FastAPI
<<<<<<< HEAD
from fastapi.security import OAuth2PasswordBearer
from app.routes import book as book_routes


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
=======

from app import database as db
from app.routes import book as book_routes
from app.models import book

# book.Base.metadata.create_all(bind=engine)
>>>>>>> 65c530dc3ff53bccb3ee14a8f4b31d4238c52a47

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