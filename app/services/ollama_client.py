import requests
from app.config import settings

def ask_ollama(prompt: str) -> str:
    try:
        res = requests.post(
            settings.OLLAMA_URL,
            json={
                "model": settings.OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False
            }
        )
        return res.json()["response"]
    except Exception as e:
        return f"AI Error: {str(e)}"