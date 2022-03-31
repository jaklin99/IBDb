from fastapi import FastAPI
from app.routes import book

app = FastAPI()

app.include_router(book.books)
