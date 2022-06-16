from fastapi import FastAPI
from app.api.books import books
from app.api.db import metadata, database, engine
from starlette.middleware.cors import CORSMiddleware

metadata.create_all(engine)

app = FastAPI(openapi_url="/api/books/openapi.json", docs_url="/api/books/docs")

origins = {"*"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(books, prefix='/api/books', tags=['books'])