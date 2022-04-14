from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from app.routes import book as book_routes


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

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