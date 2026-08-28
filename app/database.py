import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL

load_dotenv(".env")

# Database api_fastapi
API_FASTAPI_DATABASE_URL = URL.create(
    drivername="mysql+pymysql",
    username=os.getenv("API_FASTAPI_DB_USER"),
    password=os.getenv("API_FASTAPI_DB_PASSWORD"),
    host=os.getenv("API_FASTAPI_DB_HOST"),
    port=os.getenv("API_FASTAPI_DB_PORT"),
    database=os.getenv("API_FASTAPI_DB_NAME")
)

IOT_DATABASE_URL = URL.create(
    drivername="mysql+pymysql",
    username=os.getenv("IOT_DB_USER"),
    password=os.getenv("IOT_DB_PASSWORD"),
    host=os.getenv("IOT_DB_HOST"),
    port=os.getenv("IOT_DB_PORT"),
    database=os.getenv("IOT_DB_NAME")
)

SISTEMIT_DATABASE_URL = URL.create(
    drivername="mysql+pymysql",
    username=os.getenv("SISTEMIT_DB_USER"),
    password=os.getenv("SISTEMIT_DB_PASSWORD"),
    host=os.getenv("SISTEMIT_DB_HOST"),
    port=os.getenv("SISTEMIT_DB_PORT"),
    database=os.getenv("SISTEMIT_DB_NAME")
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