from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_iot_db
from app.model import Device
from app.schema import DeviceResponse
from app.auth import get_current_user


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

    devices = (
        db.query(Device)
        .order_by(Device.device_name)
        .all()
    )

    return devices