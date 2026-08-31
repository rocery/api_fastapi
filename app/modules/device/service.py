from datetime import datetime
from sqlalchemy.orm import Session

from app.modules.device.model import Device, IspSpeedtest


def list_devices(db: Session):
    return (
        db.query(Device)
        .order_by(Device.device_name)
        .all()
    )

def isp_speedtest_list(
    db: Session,
    server: str | None = None,
    period: str | None = None,
):
    query = (
        db.query(IspSpeedtest)
        .order_by(IspSpeedtest.created_at.desc())
    )

    # Filter server
    if server:
        query = query.filter(
            IspSpeedtest.server == server
        )

    # Filter bulan-tahun
    if period:
        start_date = datetime.strptime(period, "%Y-%m")

        if start_date.month == 12:
            end_date = start_date.replace(
                year=start_date.year + 1,
                month=1
            )
        else:
            end_date = start_date.replace(
                month=start_date.month + 1
            )

        query = query.filter(
            IspSpeedtest.created_at >= start_date,
            IspSpeedtest.created_at < end_date,
        )

    return query.all()