# logic.py

import random  # for choosing a random word

# Load words from file and return as a list
def load_words(file_path):
    # open the file and read all lines
    with open(file_path, 'r') as f:
        words = [line.strip() for line in f]  # remove newline characters
    return words  # return the list of words

# Pick a random word from the list
def choose_word(words):
    return random.choice(words)  # randomly pick one word

# Show the current guessed state of the word
def render_word(secret, guessed):
    display = ""
    for letter in secret:
        if letter in guessed:  # if player guessed this letter
            display += letter + " "  # show the letter
        else:
            display += "_ "  # hide the letter
    return display.strip()  # remove extra space at the end

# Check if player has guessed all letters
def is_win(secret, guessed):
    return all(letter in guessed for letter in secret)  # True if all letters guessed
