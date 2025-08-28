from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    GROQ_API_KEY = os.getenv("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")
    TAVILY_API_KEY = os.getenv("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")

    ALLOWED_MODEL_NAMES =[
        "llama3-70b-8192",
        "llama-3.3-70b-versatile"
    ]

settings=Settings()
