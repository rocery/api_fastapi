import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv("../.env")

db_url = os.getenv("DB_HOST")
print(f"Database URL: {db_url}")