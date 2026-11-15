import re
import json

# Colors
GREEN = "\033[92m"
BLUE = "\033[94m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"
BOLD = "\033[1m"


# Load FAQ dataset
def load_faq():
    try:
        with open("sample_faq.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        print(RED + "Error: faq.json file not found!" + RESET)
        return {"greetings": [], "faqs": []}

    except json.JSONDecodeError:
        print(RED + "Error: Invalid JSON file!" + RESET)
        return {"greetings": [], "faqs": []}


data = load_faq()


# Normalize text
def normalize_text(text):
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    return text


# Get chatbot response
def get_response(user_input):

    text = normalize_text(user_input)

    if not text:
        return "Please enter a valid question."

    # Exit commands
    if re.fullmatch(r"(bye|exit|quit)", text):
        return "Thank you for contacting Datheon. Have a great day!"

    responses = []

    # Greeting detection
    for greeting in data["greetings"]:
        if re.search(r"\b" + re.escape(greeting) + r"\b", text):
            responses.append(
                "Hello! Welcome to Datheon Support. How can I help you?"
            )
            break

    # Stop words
    stop_words = {
        "what", "are", "your", "how", "do", "i",
        "when", "will", "the", "is", "a", "to",
        "my", "you", "and", "of", "for", "can"
    }

    user_words = set(text.split()) - stop_words

    # Match FAQ questions
    for faq in data["faqs"]:

        question = normalize_text(faq["question"])
        faq_words = set(question.split()) - stop_words

        common_words = user_words.intersection(faq_words)

        if len(common_words) >= 2:
            responses.append(faq["answer"])

    # Remove duplicate responses
    responses = list(dict.fromkeys(responses))

    if responses:
        return "\n".join(responses)

    return (
        "Sorry, I could not understand your question.\n"
        "Please ask about business hours, project submission "
        "or certificate details."
    )


# Main chatbot
def chatbot():

    print("\n" + CYAN + "=" * 55 + RESET)
    print(BOLD + GREEN + "          DATHEON CUSTOMER SUPPORT" + RESET)
    print(BOLD + YELLOW + "               PYTHON CHATBOT" + RESET)
    print(CYAN + "=" * 55 + RESET)

    print("\n" + BLUE + "  Welcome! How can I assist you today?" + RESET)

    print(YELLOW + "\n  Available Topics:" + RESET)
    print("  1. Business Hours")
    print("  2. Internship Project Submission")
    print("  3. Certificate Information")

    print(RED + "\n  Type 'bye' to exit the chatbot." + RESET)
    print(CYAN + "-" * 55 + RESET)

    while True:

        user_input = input("\n" + GREEN + "  You  >> " + RESET)

        response = get_response(user_input)

        if re.fullmatch(r"(bye|exit|quit)", normalize_text(user_input)):
            print("\n" + YELLOW + "  Bot  >> " + response + RESET)
            print(CYAN + "\n" + "=" * 55 + RESET)
            print(GREEN + "       Thank you for using Datheon Support!" + RESET)
            print(CYAN + "=" * 55 + RESET)
            break

        print("\n" + BLUE + "  Bot  >> " + RESET + response)


if __name__ == "__main__":
    chatbot()
