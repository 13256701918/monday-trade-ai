# app/core/config.py
from pydantic_settings import BaseSettings
from pydantic import SecretStr

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Starter"
    API_V1_PREFIX: str = "/api/v1"

    OPENAI_API_KEY: SecretStr
    OPENAI_BASE_URL: str | None = None
    OPENAI_MODEL: str = "gpt-4o-mini"   # or what you prefer

    class Config:
        env_file = ".env"

settings = Settings()