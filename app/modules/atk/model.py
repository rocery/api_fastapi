from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

SistemitBase = declarative_base()


class Atk(SistemitBase):
    __tablename__ = "atk"

    id = Column(Integer, primary_key=True)
    varian = Column(String(2))
    item = Column(String(250))
    satuan = Column(String(20))
    harga = Column(Float)
