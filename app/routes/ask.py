from fastapi import APIRouter
from app.services.search_service import search_faq
from app.services.ai_service import generate_answer

router = APIRouter()

@router.post("/")
async def ask_question(payload: dict):

    question = payload.get("question")

    # Step 1: semantic search (embedding-based)
    match = await search_faq(question)

    # Step 2: if match found
    if match:
        return {
            "answer": match["answer"],
            "source": "embedding_db",
            "category": match.get("category", "general")
        }

    # Step 3: fallback to AI
    ai_answer = generate_answer(question, [])

    return {
        "answer": ai_answer,
        "source": "ollama_ai",
        "category": "unknown"
    }