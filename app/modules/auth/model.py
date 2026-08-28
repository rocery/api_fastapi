from sqlalchemy import Column, BigInteger, String, DateTime
from sqlalchemy.orm import declarative_base

UserBase = declarative_base()


class User(UserBase):
    __tablename__ = "user"

    user_id = Column(BigInteger, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    name = Column(String(100))
    email = Column(String(100), unique=True)
    level = Column(String(100), nullable=False)
    created_date = Column(DateTime)
