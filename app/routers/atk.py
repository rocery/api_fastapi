from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_sistemit_db
from app.model import Atk
from app.schema import AtkResponse
from app.auth import get_current_user


router = APIRouter(
    prefix="/atk",
    tags=["ATK"]
)


@router.get(
    "",
    response_model=list[AtkResponse]
)
def list_atk(
    db: Session = Depends(get_sistemit_db),
    current_user = Depends(get_current_user)
):

    items = (
        db.query(Atk)
        .order_by(Atk.item)
        .all()
    )

    return items