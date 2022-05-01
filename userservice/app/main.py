from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from starlette.middleware.cors import CORSMiddleware

from .routes import user

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="token",
    scopes={"me": "Read information about the current user.", "items": "Read items."},
)

app = FastAPI()

origins = ["*"]

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
