from sqlalchemy import Column, BigInteger, Integer, String, Text, Float, DateTime
from sqlalchemy.orm import declarative_base

UserBase = declarative_base()
IotBase = declarative_base()
SistemitBase = declarative_base()


class User(UserBase):
    __tablename__ = "user"

    user_id = Column(BigInteger, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    name = Column(String(100))
    email = Column(String(100), unique=True)
    level = Column(String(100), nullable=False)
    created_date = Column(DateTime)


class Device(IotBase):
    __tablename__ = "device"

    device_id = Column(String(20), primary_key=True)
    device_name = Column(String(50), unique=True, nullable=False)
    ip_address = Column(String(20), unique=True, nullable=False)
    location = Column(String(50), nullable=False)
    etc = Column(Text, nullable=False)
    ping = Column(String(150))


class Atk(SistemitBase):
    __tablename__ = "atk"

    id = Column(Integer, primary_key=True)
    varian = Column(String(2))
    item = Column(String(250))
    satuan = Column(String(20))
    harga = Column(Float)