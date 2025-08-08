# app/api/v1/routes.py
import openai
from fastapi import APIRouter
from typing import Optional
from fastapi import HTTPException
from pydantic import BaseModel
from openai import OpenAI
from app.core.config import settings
router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "ok"}

class QAIn(BaseModel):
    question: str

@router.post("/qa")
async def simple_qa(body: QAIn):
    # Read API key from settings (.env)
    api_key: Optional[str] = settings.OPENAI_API_KEY.get_secret_value() if settings.OPENAI_API_KEY else None
    if not api_key:
        raise HTTPException(status_code=500, detail="OPENAI_API_KEY not set; add it to your .env")
    print(api_key)
    openai.api_key = api_key
    # Client (support custom base URL if you use a proxy)
    if settings.OPENAI_BASE_URL:
        client = OpenAI(api_key=api_key, base_url=settings.OPENAI_BASE_URL)
    else:
        client = OpenAI(api_key=api_key)

    model = settings.OPENAI_MODEL or "gpt-4o-mini"

    resp = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a concise assistant."},
            {"role": "user", "content": body.question},
        ],
    )
    return {"answer": resp.choices[0].message.content}