from sqlalchemy.orm import Session

from app.modules.device.model import Device


def list_devices(db: Session):
    return (
        db.query(Device)
        .order_by(Device.device_name)
        .all()
    )
