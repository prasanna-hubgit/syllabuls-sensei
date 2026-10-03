
from app.rag import RAGSystem


class SyllabusSensei:
    """
    Deerwalk FAQ chatbot for Syllabus Sensei.
    """

    def __init__(self):
        self.name = "Syllabus Sensei"
        self.rag = RAGSystem()

    def respond(self, message: str) -> str:
        message = message.strip()

        if not message:
            return "Please ask me a question about Deerwalk."

        results = self.rag.search(message, top_k=5)

        if not results:
            return (
                "I'm currently designed to answer questions about "
                "Deerwalk Sifal School, its streams, subjects, and courses."
            )

        for result in results:
            data = result["data"]

            if "faqs" in data:
                faq = self.find_best_faq(message, data["faqs"])

                if faq:
                    return faq["answer"]

        return (
            "I couldn't find a relevant answer in my Deerwalk FAQ yet."
        )

    def find_best_faq(self, message: str, faqs):
        """
        Find the FAQ that best matches the student's question.
        """

        message_words = {
            word.lower().strip(".,?!:;()[]{}")
            for word in message.split()
            if len(word) > 2
        }

        best_faq = None
        best_score = 0

        for faq in faqs:
            question_words = {
                word.lower().strip(".,?!:;()[]{}")
                for word in faq["question"].split()
                if len(word) > 2
            }

            score = len(
                message_words.intersection(question_words)
            )

            if score > best_score:
                best_score = score
                best_faq = faq

        return best_faq

