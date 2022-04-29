from fastapi import FastAPI
from app.routes import book as book_routes


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