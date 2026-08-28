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

