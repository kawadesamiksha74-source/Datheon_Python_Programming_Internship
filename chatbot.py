import re
import json
import os

# Load FAQ dataset
def load_faq():
    try:
        with open("sample_faq.json", "r") as file:
            data = json.load(file)
        return data

    except FileNotFoundError:
        print("Error: sample_faq.json file not found!")
        return {"greetings": [], "faqs": []}

    except json.JSONDecodeError:
        print("Error: Invalid JSON file!")
        return {"greetings": [], "faqs": []}


data = load_faq()


# Normalize user input
def normalize_text(text):
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    return text


# Check user query
def get_response(user_input):

    text = normalize_text(user_input)

    if not text:
        return "Please enter a valid question."

    # Exit commands
    if re.search(r"\b(bye|exit|quit)\b", text):
        return "Thank you for contacting Datheon. Goodbye!"

    # Greeting detection
    for greeting in data["greetings"]:
        if re.search(r"\b" + re.escape(greeting) + r"\b", text):
            return "Hello! Welcome to Datheon Support. How can I help you?"

    # Match FAQ questions
    matched_answers = []

    stop_words = {
        "what", "are", "your", "how", "do", "i",
        "when", "will", "the", "is", "a", "to",
        "my", "you", "and", "of", "for"
    }

    user_words = set(text.split()) - stop_words

    for faq in data["faqs"]:

        question = normalize_text(faq["question"])
        faq_words = set(question.split()) - stop_words

        common_words = user_words.intersection(faq_words)

        if len(common_words) >= 2:
            matched_answers.append(faq["answer"])

    # Multi-intent response
    if matched_answers:
        return "\n".join(matched_answers)

    # Fallback response
    return (
        "Sorry, I could not understand your question. "
        "Please ask about business hours, project submission "
        "or certificate details."
    )


# Main chatbot
def chatbot():

    print("=" * 45)
    print("       DATHEON CUSTOMER SUPPORT CHATBOT")
    print("=" * 45)

    print("Bot: Hello! Welcome to Datheon Support.")
    print("Bot: Type bye, exit or quit to stop.\n")

    while True:

        user_input = input("You: ")

        response = get_response(user_input)

        print("Bot:", response)

        if re.search(r"\b(bye|exit|quit)\b", user_input.lower()):
            break


if __name__ == "__main__":
    chatbot()