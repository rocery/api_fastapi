from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.sistemit import get_sistemit_db
from app.modules.atk.schema import AtkResponse
from app.modules.atk.service import list_atk as list_atk_service
from app.core.security import get_current_user


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

    return list_atk_service(db)
