from sqlalchemy import Column, String, Text
from sqlalchemy.orm import declarative_base

IotBase = declarative_base()


class Device(IotBase):
    __tablename__ = "device"

    device_id = Column(String(20), primary_key=True)
    device_name = Column(String(50), unique=True, nullable=False)
    ip_address = Column(String(20), unique=True, nullable=False)
    location = Column(String(50), nullable=False)
    etc = Column(Text, nullable=False)
    ping = Column(String(150))
