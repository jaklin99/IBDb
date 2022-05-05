from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.routes import book as book_routes


app = FastAPI()

origins = {"http://localhost:3000"
}

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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