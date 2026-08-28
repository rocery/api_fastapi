from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL

from app.core.config import (
    API_FASTAPI_DB_USER,
    API_FASTAPI_DB_PASSWORD,
    API_FASTAPI_DB_HOST,
    API_FASTAPI_DB_PORT,
    API_FASTAPI_DB_NAME,
)

API_FASTAPI_DATABASE_URL = URL.create(
    drivername="mysql+pymysql",
    username=API_FASTAPI_DB_USER,
    password=API_FASTAPI_DB_PASSWORD,
    host=API_FASTAPI_DB_HOST,
    port=API_FASTAPI_DB_PORT,
    database=API_FASTAPI_DB_NAME
)

api_fastapi_engine = create_engine(
    API_FASTAPI_DATABASE_URL,
    pool_pre_ping=True,
)

ApiFastapiSessionLocal = sessionmaker(
    bind=api_fastapi_engine,
    autocommit=False,
    autoflush=False,
)

def get_api_fastapi_db():
    db = ApiFastapiSessionLocal()
    try:
        yield db
    finally:
        db.close()
