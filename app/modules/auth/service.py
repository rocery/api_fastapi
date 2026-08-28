from sqlalchemy.orm import Session

from app.core.security import md5_password
from app.modules.auth.model import User


def authenticate_user(
    db: Session,
    username: str,
    password: str
):
    user = (
        db.query(User)
        .filter(User.username == username)
        .first()
    )

    if not user:
        return None

    password_md5 = md5_password(password)

    if user.password != password_md5:
        return None

    return user
