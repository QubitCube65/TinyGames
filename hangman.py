import nltk
from nltk.corpus import words
import random

board = [
    """
    +---+
    |   |
        |
        |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
        |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    =========
    """
]

class Hangman:
    def __init__(self, word):
        self.word = word.lower()
        self.missed_letters = []
        self.guessed_letters = []

    def guess(self, letter):
        letter = letter.lower()
        if letter in self.word and letter not in self.guessed_letters:
            self.guessed_letters.append(letter)
        elif letter not in self.word and letter not in self.missed_letters:
            self.missed_letters.append(letter)
        else:
            return False
        return True

    def hangman_over(self):
        return self.hangman_won() or (len(self.missed_letters) == 6)

    def hangman_won(self):
        return "_" not in self.hide_word()

    def hide_word(self):
        return " ".join(letter if letter in self.guessed_letters else "_" for letter in self.word)

    def print_game_status(self):
        print(board[len(self.missed_letters)])
        print("Word: " + self.hide_word())
        print("Missed letters: ", " ".join(self.missed_letters))
        print("Guessed letters: ", " ".join(self.guessed_letters))
        print()

def rand_word():
    word_list = words.words()                 #nltk
    return random.choice(word_list).lower()

def main():
    game = Hangman(rand_word())
    while not game.hangman_over():
        game.print_game_status()
        user_input = input("\nEnter a letter: ").strip().lower()
        if len(user_input) != 1 or not user_input.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        game.guess(user_input)
    
    game.print_game_status()
    if game.hangman_won():
        print("\nCongratulations! You won the game.")
    else:
        print("\nOh no, you lost.")
        print("\nThe word was: " + game.word)
    
    print("Thank you for playing!\n")

if __name__ == "__main__":
    main()

        
      