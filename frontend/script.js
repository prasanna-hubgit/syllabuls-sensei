const pages = document.querySelectorAll(".page");
const previousButton = document.getElementById("previous-button");
const nextButton = document.getElementById("next-button");
const pageNumber = document.getElementById("page-number");

let currentPage = 0;

function showPage(pageIndex) {
    if (pageIndex < 0) {
        pageIndex = 0;
    }

    if (pageIndex >= pages.length) {
        pageIndex = pages.length - 1;
    }

    currentPage = pageIndex;

    pages.forEach((page, index) => {
        page.classList.toggle(
            "active",
            index === currentPage
        );
    });

    pageNumber.textContent =
        `${currentPage + 1} / ${pages.length}`;

    previousButton.disabled = currentPage === 0;
    nextButton.disabled =
        currentPage === pages.length - 1;
}


/* Page navigation */

function nextPage() {
    if (currentPage < pages.length - 1) {
        showPage(currentPage + 1);
    }
}

function previousPage() {
    if (currentPage > 0) {
        showPage(currentPage - 1);
    }
}


/* Arrow keys */

document.addEventListener("keydown", (event) => {

    const activeElement = document.activeElement;

    if (
        activeElement &&
        (
            activeElement.tagName === "TEXTAREA" ||
            activeElement.tagName === "INPUT"
        )
    ) {
        return;
    }

    if (event.key === "ArrowRight") {
        nextPage();
    }

    if (event.key === "ArrowLeft") {
        previousPage();
    }
});


/* Floating maths and programming text */

const background =
    document.getElementById("academic-background");

const mathItems = [
    "x² + 4x + 4",
    "∫₀¹ x² dx",
    "F ma",
    "v u + at",
    "E mc²",
    "A πr²",
    "sin θ",
    "quadratic formula",
    "Newton's laws",
    "linear algebra",
    "probability",
    "vectors",
    "√(x² + y²)",
    "Δv",
    "f(x)"
];

const codeItems = [
    "def calculate_area",
    "return result",
    "for number in numbers",
    "print number",
    "class Student",
    "import math",
    "calculate result",
    "student marks",
    "solve problem",
    "data processing",
    "python programming",
    "computer science",
    "student database",
    "function result"
];

function createFloatingItem() {

    const item = document.createElement("div");

    const isCode = Math.random() < 0.4;
    const items = isCode ? codeItems : mathItems;

    item.textContent =
        items[Math.floor(Math.random() * items.length)];

    item.className = "floating-item";

    if (isCode) {
        item.classList.add("code");
    }

    item.style.left =
        `${Math.random() * 100}%`;

    item.style.fontSize =
        `${12 + Math.random() * 8}px`;

    item.style.animationDuration =
        `${18 + Math.random() * 22}s`;

    item.style.animationDelay =
        `${Math.random() * -25}s`;

    background.appendChild(item);
}

for (let i = 0; i < 22; i++) {
    createFloatingItem();
}


/* FAQ AI */

const CHAT_API_URL =
    "https://37b68c46-8000.inc1.devtunnels.ms/chat";

const faqButtons =
    document.querySelectorAll(".faq-ai-item");

const faqChatForm =
    document.getElementById("faq-chat-form");

const faqChatInput =
    document.getElementById("faq-chat-input");

const faqChatArea =
    document.getElementById("faq-chat-area");


function addFaqMessage(message, className) {

    const messageBox =
        document.createElement("div");

    messageBox.className =
        `faq-chat-message ${className}`;

    const paragraph =
        document.createElement("p");

    paragraph.textContent = message;

    messageBox.appendChild(paragraph);

    faqChatArea.appendChild(messageBox);

    faqChatArea.scrollTop =
        faqChatArea.scrollHeight;

    return messageBox;
}


async function askSensei(message) {

    addFaqMessage(message, "user-message");

    const thinkingMessage =
        addFaqMessage(
            "Sensei is thinking...",
            "sensei-message"
        );

    try {

        const response = await fetch(
            CHAT_API_URL,
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    message: message
                })
            }
        );

        if (!response.ok) {
            throw new Error("Server request failed.");
        }

        const data =
            await response.json();

        thinkingMessage
            .querySelector("p")
            .textContent =
            data.reply;

    } catch (error) {

        thinkingMessage
            .querySelector("p")
            .textContent =
            "Could not connect to Syllabus Sensei. Make sure the backend is running.";

    }
}


/* Clickable FAQ questions */

faqButtons.forEach((button) => {

    button.addEventListener("click", () => {

        const question =
            button.dataset.question;

        if (question) {
            askSensei(question);
        }

    });

});


/* Chat input */

if (faqChatForm) {

    faqChatForm.addEventListener(
        "submit",
        (event) => {

            event.preventDefault();

            const message =
                faqChatInput.value.trim();

            if (!message) {
                return;
            }

            faqChatInput.value = "";

            askSensei(message);
        }
    );

}


showPage(0);
