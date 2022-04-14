from fastapi import FastAPI
from app.routes import review

app = FastAPI()

<<<<<<< HEAD
app.include_router(review.r_router)
=======
app.include_router(review.r_router)
>>>>>>> 65c530dc3ff53bccb3ee14a8f4b31d4238c52a47
