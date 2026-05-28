from fastapi import APIRouter
from app.database import faq_collection
from app.schemas.faq_schema import FAQCreate
from app.utils.embeddings import get_embedding

router = APIRouter()

@router.post("/")
async def create_faq(faq: FAQCreate):

    embedding = get_embedding(faq.question)

    data = faq.dict()
    data["embedding"] = embedding

    result = await faq_collection.insert_one(data)

    return {
        "id": str(result.inserted_id),
        "message": "FAQ created with embedding"
    }

@router.get("/")
async def get_all_faqs():
    faqs = await faq_collection.find().to_list(length=100)

    for faq in faqs:
        faq["id"] = str(faq["_id"])
        del faq["_id"]

    return faqs