from fastapi import APIRouter, Depends, Form, Request, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.model import Users
from app.dependencies import get_current_user


router = APIRouter()


@router.post("/login")
def login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    user = (
        db.query(Users)
        .filter(
            Users.username == username,
            Users.password == password
        )
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Username atau password salah"
        )

    request.session["user_id"] = user.id

    return {
        "message": "Login berhasil",
        "user": {
            "id": user.id,
            "username": user.username,
            "name": user.name,
            "level": user.level
        }
    }


@router.get("/dashboard")
def dashboard(
    user=Depends(get_current_user)
):
    return {
        "message": "Selamat datang di dashboard",
        "user": user
    }


@router.post("/logout")
def logout(request: Request):
    request.session.clear()

    return {
        "message": "Logout berhasil"
    }
    
@router.get("/me")
def me(
    request: Request,
    db: Session = Depends(get_db)
):
    user_id = request.session.get("user_id")

    if not user_id:
        raise HTTPException(401, "Unauthorized")

    user = db.query(Users).filter(Users.id == user_id).first()

    if not user:
        raise HTTPException(401, "User tidak ditemukan")

    return {
        "id": user.id,
        "username": user.username,
        "name": user.name,
        "level": user.level
    }