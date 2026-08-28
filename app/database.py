import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv("../.env")

# Database api_fastapi
API_FASTAPI_DATABASE_URL = (
    f"mysql+pymysql://"
    f"{os.getenv('API_FASTAPI_DB_USER')}:{os.getenv('API_FASTAPI_DB_PASSWORD')}"
    f"@{os.getenv('API_FASTAPI_DB_HOST')}:{os.getenv('API_FASTAPI_DB_PORT')}"
    f"/{os.getenv('API_FASTAPI_DB_NAME')}"
)

IOT_DATABASE_URL = (
    f"mysql+pymysql://"
    f"{os.getenv('IOT_DB_USER')}:{os.getenv('IOT_DB_PASSWORD')}"
    f"@{os.getenv('IOT_DB_HOST')}:{os.getenv('IOT_DB_PORT')}"
    f"/{os.getenv('IOT_DB_NAME')}"
)

SISTEMIT_DATABASE_URL = (
    f"mysql+pymysql://"
    f"{os.getenv('SISTEMIT_DB_USER')}:{os.getenv('SISTEMIT_DB_PASSWORD')}"
    f"@{os.getenv('SISTEMIT_DB_HOST')}:{os.getenv('SISTEMIT_DB_PORT')}"
    f"/{os.getenv('SISTEMIT_DB_NAME')}"
)

api_fastapi_engine = create_engine(
    API_FASTAPI_DATABASE_URL,
    pool_pre_ping=True,
)

iot_engine = create_engine(
    IOT_DATABASE_URL,
    pool_pre_ping=True,
)

sistemit_engine = create_engine(
    SISTEMIT_DATABASE_URL,
    pool_pre_ping=True,
)


ApiFastapiSessionLocal = sessionmaker(
    bind=api_fastapi_engine,
    autocommit=False,
    autoflush=False,
)

IotSessionLocal = sessionmaker(
    bind=iot_engine,
    autocommit=False,
    autoflush=False,
)

SistemitSessionLocal = sessionmaker(
    bind=sistemit_engine,
    autocommit=False,
    autoflush=False,
)

def get_api_fastapi_db():
    db = ApiFastapiSessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_iot_db():
    db = IotSessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_sistemit_db():
    db = SistemitSessionLocal()
    try:
        yield db
    finally:
        db.close()