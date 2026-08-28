import os

from dotenv import load_dotenv
from fastapi import FastAPI

from starlette.middleware.sessions import SessionMiddleware

from app.routers.auth import router as auth_router


load_dotenv()

app = FastAPI()


app.add_middleware(
    SessionMiddleware,
    secret_key=os.getenv("SESSION_SECRET")
)


app.include_router(auth_router)


@app.get("/")
def root():
    return {
        "message": "FastAPI Auth"
    }