from sqlalchemy.orm import Session

from app.modules.atk.model import Atk


def list_atk(db: Session):
    return (
        db.query(Atk)
        .order_by(Atk.item)
        .all()
    )
