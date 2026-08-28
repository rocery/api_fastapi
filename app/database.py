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
