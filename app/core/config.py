import os

from dotenv import load_dotenv

load_dotenv(".env")

SECRET_KEY = os.getenv("SECRET_KEY")
SESSION_SECRET = os.getenv("SESSION_SECRET")
ALGORITHM = "HS256"

# api_fastapi DB env
API_FASTAPI_DB_USER = os.getenv("API_FASTAPI_DB_USER")
API_FASTAPI_DB_PASSWORD = os.getenv("API_FASTAPI_DB_PASSWORD")
API_FASTAPI_DB_HOST = os.getenv("API_FASTAPI_DB_HOST")
API_FASTAPI_DB_PORT = os.getenv("API_FASTAPI_DB_PORT")
API_FASTAPI_DB_NAME = os.getenv("API_FASTAPI_DB_NAME")

# iot DB env
IOT_DB_USER = os.getenv("IOT_DB_USER")
IOT_DB_PASSWORD = os.getenv("IOT_DB_PASSWORD")
IOT_DB_HOST = os.getenv("IOT_DB_HOST")
IOT_DB_PORT = os.getenv("IOT_DB_PORT")
IOT_DB_NAME = os.getenv("IOT_DB_NAME")

# sistemit DB env
SISTEMIT_DB_USER = os.getenv("SISTEMIT_DB_USER")
SISTEMIT_DB_PASSWORD = os.getenv("SISTEMIT_DB_PASSWORD")
SISTEMIT_DB_HOST = os.getenv("SISTEMIT_DB_HOST")
SISTEMIT_DB_PORT = os.getenv("SISTEMIT_DB_PORT")
SISTEMIT_DB_NAME = os.getenv("SISTEMIT_DB_NAME")
