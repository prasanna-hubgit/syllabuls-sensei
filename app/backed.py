from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.chatbot import SyllabusSensei


app = FastAPI(
    title="Syllabus Sensei",
    version="0.1.0"
)


# Allow the frontend to communicate with the backend.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str


# Create the chatbot once when the server starts.
chatbot = SyllabusSensei()


@app.get("/")
def home():
    return {
        "message": "Syllabus Sensei backend is running!"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.post("/chat")
def chat(request: ChatRequest):
    reply = chatbot.respond(request.message)

    return {
        "reply": reply
    }
