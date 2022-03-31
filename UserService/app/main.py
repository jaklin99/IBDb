from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from app.routes import user


# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


app = FastAPI()

app.include_router(user.users)


# @app.get("/items/")
# async def read_items(token: str = Depends(oauth2_scheme)):
#     return {"token": token}
