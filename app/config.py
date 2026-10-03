from pathlib import Path
import os

from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Main project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Data directories
DATA_DIR = BASE_DIR / "data"
KNOWLEDGE_DIR = DATA_DIR / "knowledge"
DOCUMENTS_DIR = DATA_DIR / "documents"

# Project information
APP_NAME = "Syllabus Sensei"
APP_VERSION = "0.1.0"

# OpenAI configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
AI_MODEL = os.getenv("AI_MODEL", "")

