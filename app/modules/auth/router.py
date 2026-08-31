from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.api_fastapi import get_api_fastapi_db
from app.modules.auth.schema import LoginRequest, LoginResponse
from app.modules.auth.service import authenticate_user
from app.core.security import create_access_token, get_current_user


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
    
@router.get("/me")
def get_current_user_info(
    current_user=Depends(get_current_user)
):
    return {
        "user_id": current_user.user_id,
        "username": current_user.username,
        "name": current_user.name,
        "email": current_user.email,
        "level": current_user.level,
        "created_date": current_user.created_date
    }
