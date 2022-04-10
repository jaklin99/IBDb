from fastapi import FastAPI
from app.routes import review

app = FastAPI()

app.include_router(review.r_router)