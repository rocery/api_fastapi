from fastapi import FastAPI

from app.modules.auth.router import router as auth_router
from app.modules.device.router import router as device_router
from app.modules.atk.router import router as atk_router


app = FastAPI(
    title="Simple FastAPI API",
    version="1.0.0"
)


app.include_router(auth_router)
app.include_router(device_router)
app.include_router(atk_router)


@app.get("/")
def root():

    return {
        "message": "FastAPI API is running"
    }