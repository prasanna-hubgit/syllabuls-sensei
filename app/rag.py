import json
from pathlib import Path

from app.config import KNOWLEDGE_DIR


class RAGSystem:
    """
    Simple local knowledge-retrieval system for Syllabus Sensei.

    It searches the Deerwalk knowledge JSON files and returns
    the most relevant information for a user's question.
    """

    def __init__(self):
        self.knowledge = []
        self.load_knowledge()

    def load_knowledge(self):
        """Load all JSON knowledge files from the knowledge directory."""
        self.knowledge = []

        if not KNOWLEDGE_DIR.exists():
            return

        for file_path in KNOWLEDGE_DIR.glob("*.json"):
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    data = json.load(file)

                self.knowledge.append({
                    "source": file_path.name,
                    "data": data
                })

            except (json.JSONDecodeError, OSError) as error:
                print(f"Could not load {file_path.name}: {error}")

    def search(self, query: str, top_k: int = 5):
        """
        Search the knowledge base using simple keyword matching.
        """

        if not query.strip():
            return []

        query_words = set(
            word.lower().strip(".,?!:;()[]{}")
            for word in query.split()
            if len(word) > 2
        )

        results = []

        for item in self.knowledge:
            text = json.dumps(item["data"], ensure_ascii=False).lower()

            score = sum(
                1 for word in query_words
                if word in text
            )

            if score > 0:
                results.append({
                    "source": item["source"],
                    "score": score,
                    "data": item["data"]
                })

        results.sort(
            key=lambda result: result["score"],
            reverse=True
        )

        return results[:top_k]

    def get_context(self, query: str, top_k: int = 5):
        """Return relevant knowledge as readable context."""

        results = self.search(query, top_k)

        if not results:
            return "No relevant Deerwalk information was found."

        context = []

        for result in results:
            context.append(
                f"Source: {result['source']}\n"
                f"Information: {json.dumps(result['data'], ensure_ascii=False)}"
            )

        return "\n\n".join(context)
    