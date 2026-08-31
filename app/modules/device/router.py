from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.database.iot import get_iot_db
from app.modules.device.schema import DeviceResponse, IspSpeedtestResponse
from app.modules.device.service import isp_speedtest_list, list_devices as list_devices_service
from app.core.security import get_current_user

router = APIRouter(
    prefix="/devices",
    tags=["Device"]
)

@router.get(
    "/list",
    response_model=list[DeviceResponse]
)
def list_devices(
    db: Session = Depends(get_iot_db),
    current_user = Depends(get_current_user)
):
    return list_devices_service(db)

@router.get(
    "/isp_speedtest", 
    response_model=list[IspSpeedtestResponse]
)
def list_isp_speedtests(
    server: str | None = Query(default=None),
    period: str | None = Query(
        default=None,
        pattern=r"^\d{4}-(0[1-9]|1[0-2])$"
    ),
    db: Session = Depends(get_iot_db),
    current_user=Depends(get_current_user),
):
    return isp_speedtest_list(
        db=db,
        server=server,
        period=period,
    )
