from pydantic import BaseModel
from typing import Optional

class FAQCreate(BaseModel):
    question: str
    answer: str
    category: Optional[str] = "general"
    tags: Optional[list[str]] = []

class FAQResponse(BaseModel):
    id: str
    question: str
    answer: str
    category: str
    tags: list[str]