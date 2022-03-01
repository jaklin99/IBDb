import uvicorn
from fastapi import FastAPI

import books

# register new routes file
app = FastAPI()

app.include_router(books.books)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)