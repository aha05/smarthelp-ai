from app.services.ollama_client import ask_ollama
from app.utils.prompt_builder import build_prompt

def generate_answer(question: str, context_faqs: list):
    return ask_ollama(build_prompt(question=question,  faqs=context_faqs))