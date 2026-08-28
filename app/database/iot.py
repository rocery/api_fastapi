from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL

from app.core.config import (
    IOT_DB_USER,
    IOT_DB_PASSWORD,
    IOT_DB_HOST,
    IOT_DB_PORT,
    IOT_DB_NAME,
)

IOT_DATABASE_URL = URL.create(
    drivername="mysql+pymysql",
    username=IOT_DB_USER,
    password=IOT_DB_PASSWORD,
    host=IOT_DB_HOST,
    port=IOT_DB_PORT,
    database=IOT_DB_NAME
)

iot_engine = create_engine(
    IOT_DATABASE_URL,
    pool_pre_ping=True,
)

IotSessionLocal = sessionmaker(
    bind=iot_engine,
    autocommit=False,
    autoflush=False,
)

def get_iot_db():
    db = IotSessionLocal()
    try:
        yield db
    finally:
        db.close()
