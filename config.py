
import os

class Config:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY", "default_key")
    API_BASE_URL = os.getenv("API_BASE_URL", "https://api.groq.com/openai/v1")
    UPLOAD_DIR = "backend/uploads"

config = Config()
