from sentence_transformers import SentenceTransformer
import numpy as np

# Load model once (important for performance)
model = SentenceTransformer("all-MiniLM-L6-v2")


def get_embedding(text: str):
    """Convert text to vector embedding"""
    return model.encode(text).tolist()


def cosine_similarity(vec1, vec2):
    """Compare two embeddings"""
    v1 = np.array(vec1)
    v2 = np.array(vec2)

    return float(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))