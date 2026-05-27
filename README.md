# SmartHelp AI 🚀

Offline AI FAQ Helpdesk using FastAPI + Ollama

## Features
- FAQ storage system
- Smart keyword search
- AI fallback using Ollama
- Fully offline AI support

## Run

### 1. Install dependencies
pip install -r requirements.txt

### 2. Start Ollama
ollama run llama3

### 3. Start API
uvicorn app.main:app --reload

## API

POST /faq → add FAQ  
GET /faq → list FAQs  
POST /ask → ask AI question