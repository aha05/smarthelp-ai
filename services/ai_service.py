from app.services.ollama_client import ask_ollama

def generate_answer(question: str, context_faqs: list):
    context_text = ""

    for faq in context_faqs:
        context_text += f"Q: {faq['question']}\nA: {faq['answer']}\n\n"

    prompt = f"""
You are a helpful support assistant.

Use the following FAQs as context:

{context_text}

User question:
{question}

Answer clearly and briefly.
"""

    return ask_ollama(prompt)