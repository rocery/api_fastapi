from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_api_fastapi_db
from app.schema import LoginRequest, LoginResponse
from app.auth import authenticate_user, create_access_token


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/login", response_model=LoginResponse)
def login(
    data: LoginRequest,
    db: Session = Depends(get_api_fastapi_db)
):

    user = authenticate_user(
        db,
        data.username,
        data.password
    )

    if not user:

        raise HTTPException(
            status_code=401,
            detail="Username atau password salah"
        )

    token = create_access_token(user)

    return {
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "user_id": user.user_id,
            "username": user.username,
            "name": user.name,
            "email": user.email,
            "level": user.level,
        }
    }