from app.routes import ask
from fastapi import FastAPI
from app.routes import faq

app = FastAPI(title="SmartHelp AI - MongoDB Edition")

app.include_router(faq.router, prefix="/faq", tags=["FAQ"])
app.include_router(ask.router, prefix="/ask", tags=["Ask"])