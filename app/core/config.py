# app/core/config.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Starter"
    API_V1_PREFIX: str = "/api/v1"

settings = Settings()