import random

# Colour settings
RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
BOLD = "\033[1m"

WORDS = [
    "python", "computer", "internship", "programming", "developer",
    "keyboard", "database", "science", "project", "analytics",
    "function", "variable", "software", "student", "technology"
]

HANGMAN_STAGES = [
    r"""
     +---+
     |   |
         |
         |
         |
         |
    =========""",
    r"""
     +---+
     |   |
     O   |
         |
         |
         |
    =========""",
    r"""
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========""",
    r"""
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========""",
    r"""
     +---+
     |   |
     O   |
    /|\  |
         |
         |
    =========""",
    r"""
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
    =========""",
    r"""
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    ========="""
]


def display_word(secret_word, correct_guesses):
    return " ".join(
        letter.upper() if letter in correct_guesses else "_"
        for letter in secret_word
    )


def play_hangman():

    secret_word = random.choice(WORDS)
    correct_guesses = set()
    guessed_letters = set()
    wrong_guesses = 0
    max_attempts = 6

    print("\n" + MAGENTA + "=" * 45 + RESET)
    print(BOLD + CYAN + "          HANGMAN WORD GUESSING GAME" + RESET)
    print(MAGENTA + "=" * 45 + RESET)

    print(YELLOW + "\nGuess the hidden word, one letter at a time!")
    print("You have 6 chances to save yourself!" + RESET)

    while wrong_guesses < max_attempts:

        print(CYAN + HANGMAN_STAGES[wrong_guesses] + RESET)

        print("\n" + BOLD + "WORD: " + RESET +
              YELLOW + display_word(secret_word, correct_guesses) + RESET)

        print("Guessed letters:",
              ", ".join(sorted(guessed_letters)) if guessed_letters else "None")

        print(GREEN + f"Correct guesses: {len(correct_guesses)}" + RESET)
        print(RED + f"Wrong guesses left: {max_attempts - wrong_guesses}" + RESET)

        if all(letter in correct_guesses for letter in secret_word):

            print(GREEN + BOLD + "\nCONGRATULATIONS! YOU WIN!" + RESET)
            print(YELLOW + "Secret word: " + secret_word.upper() + RESET)
            return

        guess = input(CYAN + "\nEnter a letter: " + RESET).strip().lower()

        if len(guess) != 1 or not guess.isalpha() or not guess.isascii():
            print(RED + "Invalid input! Enter one English letter (A-Z)." + RESET)
            continue

        if guess in guessed_letters:
            print(YELLOW + "You already guessed this letter!" + RESET)
            continue

        guessed_letters.add(guess)

        if guess in secret_word:

            correct_guesses.add(guess)
            print(GREEN + f"Correct! '{guess.upper()}' is in the word." + RESET)

        else:

            wrong_guesses += 1
            print(RED + f"Wrong! '{guess.upper()}' is not in the word." + RESET)

    print(CYAN + HANGMAN_STAGES[max_attempts] + RESET)

    print(RED + BOLD + "\nGAME OVER! YOU LOSE!" + RESET)
    print(YELLOW + "The secret word was: " + secret_word.upper() + RESET)


def main():

    while True:

        play_hangman()

        again = input(
            CYAN + "\nWould you like to play again? (y/n): " + RESET
        ).strip().lower()

        if again != "y":

            print(GREEN + BOLD + "\nThanks for playing Hangman!")
            print("Goodbye! See you again!" + RESET)
            break

        print()


if __name__ == "__main__":
    main()
