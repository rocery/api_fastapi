from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.iot import get_iot_db
from app.modules.device.schema import DeviceResponse
from app.modules.device.service import list_devices as list_devices_service
from app.core.security import get_current_user


router = APIRouter(
    prefix="/devices",
    tags=["Device"]
)


@router.get(
    "",
    response_model=list[DeviceResponse]
)
def list_devices(
    db: Session = Depends(get_iot_db),
    current_user = Depends(get_current_user)
):

    return list_devices_service(db)
