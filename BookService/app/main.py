from fastapi import FastAPI

from app.database import engine
from app.routes import book as book_routes
from app.models import book

book.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(book_routes.books)

