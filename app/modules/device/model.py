from sqlalchemy import BigInteger, Column, Float, String, Text, DateTime
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
    
class IspSpeedtest(IotBase):
    __tablename__ = "isp_speedtest"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    isp = Column(String(50), nullable=False)
    download_mbps = Column(Float, nullable=False)
    upload_mbps= Column(Float, nullable=False)
    ping_ms = Column(Float, nullable=False)
    created_at = Column(DateTime)
    server_city = Column(String(50), nullable=False)
    server = Column(String(50))