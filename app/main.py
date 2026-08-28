from fastapi import FastAPI

from app.routers import auth
from app.routers import device
from app.routers import atk


app = FastAPI(
    title="Simple FastAPI API",
    version="1.0.0"
)


app.include_router(auth.router)
app.include_router(device.router)
app.include_router(atk.router)


@app.get("/")
def root():

    return {
        "message": "FastAPI API is running"
    }