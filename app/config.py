from dotenv import load_dotenv
import os

# load .env file
load_dotenv()

class Settings:
    MONGO_URL = os.getenv("MONGO_URL")
    DB_NAME = os.getenv("DB_NAME")

    OLLAMA_URL = os.getenv("OLLAMA_URL")
    OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")

    DEBUG = os.getenv("DEBUG", "False") == "True"

settings = Settings()