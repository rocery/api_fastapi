from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL

from app.core.config import (
    SISTEMIT_DB_USER,
    SISTEMIT_DB_PASSWORD,
    SISTEMIT_DB_HOST,
    SISTEMIT_DB_PORT,
    SISTEMIT_DB_NAME,
)

SISTEMIT_DATABASE_URL = URL.create(
    drivername="mysql+pymysql",
    username=SISTEMIT_DB_USER,
    password=SISTEMIT_DB_PASSWORD,
    host=SISTEMIT_DB_HOST,
    port=SISTEMIT_DB_PORT,
    database=SISTEMIT_DB_NAME
)

sistemit_engine = create_engine(
    SISTEMIT_DATABASE_URL,
    pool_pre_ping=True,
)

SistemitSessionLocal = sessionmaker(
    bind=sistemit_engine,
    autocommit=False,
    autoflush=False,
)

def get_sistemit_db():
    db = SistemitSessionLocal()
    try:
        yield db
    finally:
        db.close()
