from pydantic import BaseModel
from typing import List, Optional

class FAQ(BaseModel):
    question: str
    answer: str
    category: str = "general"
    tags: List[str] = []

    class Config:
        from_attributes = True