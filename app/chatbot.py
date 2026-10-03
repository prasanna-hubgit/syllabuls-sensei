from app.rag import RAGSystem


class SyllabusSensei:
    """
    Deerwalk-specific academic assistant.

    For now, Sensei uses the local knowledge base.
    Later, we can connect an AI model when API credits are available.
    """

    def __init__(self):
        self.name = "Syllabus Sensei"
        self.rag = RAGSystem()

    def respond(self, message: str) -> str:
        message = message.strip()

        if not message:
            return "Please ask me a question."

        results = self.rag.search(message)

        if not results:
            return (
                "I couldn't find that information in my Deerwalk "
                "knowledge base yet."
            )

        best_result = results[0]

        return self.format_answer(best_result)

    def format_answer(self, result):
        """Turn retrieved knowledge into a readable response."""

        data = result["data"]

        # FAQ knowledge
        if "faqs" in data:
            return self.answer_from_faq(data["faqs"])

        # Stream knowledge
        if "streams" in data:
            return self.answer_from_streams(data)

        # Subject knowledge
        if "subjects" in data:
            return self.answer_from_subjects(data["subjects"])

        # School information
        if "school" in data:
            return self.answer_from_school(data["school"])

        return "I found relevant information, but I couldn't format it yet."

    def answer_from_faq(self, faqs):
        """Return the most relevant FAQ answer."""

        return faqs[0]["answer"]

    def answer_from_streams(self, data):
        """Format stream information."""

        streams = data.get("streams", [])

        lines = ["The available +2 Science groups are:"]

        for stream in streams:
            subjects = ", ".join(stream["subjects"])
            lines.append(
                f"- {stream['name']}: {subjects}"
            )

        return "\n".join(lines)

    def answer_from_subjects(self, subjects):
        """Format subject information."""

        lines = ["Here is the relevant subject information:"]

        for subject in subjects[:5]:
            lines.append(
                f"- {subject['name']}: {subject['description']}"
            )

        return "\n".join(lines)

    def answer_from_school(self, school):
        """Format general school information."""

        return (
            f"{school['name']} ({school['short_name']}) "
            f"offers {school['level']} education in "
            f"{school['location']}."
        )
        