from app.database import faq_collection
from app.utils.embeddings import get_embedding, cosine_similarity

async def search_faq(question: str, threshold: float = 0.75):

    query_embedding = get_embedding(question)

    faqs = await faq_collection.find().to_list(length=100)

    best_match = None
    best_score = 0

    for faq in faqs:
        if "embedding" not in faq:
            continue

        score = cosine_similarity(query_embedding, faq["embedding"])

        if score > best_score:
            best_score = score
            best_match = faq

    if best_score >= threshold:
        return best_match

    return None