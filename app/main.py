# app/main.py
from fastapi import FastAPI
from app.core.config import settings
from app.api.v1.routes import router as v1_router

app = FastAPI(title=settings.PROJECT_NAME)

# Include API v1 routes
app.include_router(v1_router, prefix=settings.API_V1_PREFIX)