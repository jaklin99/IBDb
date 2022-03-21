from .database import Base
from .config import settings

from fastapi import FastAPI


def create_app():
    app = FastAPI()

    from api.routes import user
    app.include_router(user.users)

    @app.get("/home")
    def home():
        return {"message": "hello world"}

    return app
