from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from starlette.middleware.cors import CORSMiddleware

from app.routes import user

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="token"
)

app = FastAPI()

origins = {
    "http://localhost:3000",
    "http://localhost:8081",
}

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.users)

# @app.get("/items/")
# async def read_items(token: str = Depends(oauth2_scheme)):
#     return {"token": token}
#
# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8001)
