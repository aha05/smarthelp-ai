def build_prompt(question: str, faqs: list) -> str:
    context = ""

    for faq in faqs:
        context += f"Q: {faq['question']}\nA: {faq['answer']}\n\n"

    prompt = f"""
You are a professional customer support assistant.

Use ONLY the context below to answer.

Context:
{context}

User Question:
{question}

Rules:
- Be short and clear
- If unsure, say you don't know
- Do not hallucinate

Answer:
"""
    return prompt