# game.py
# main game loop

import os
import random
from .logic import load_words, choose_word, render_word, is_win

# get absolute path to words.txt
WORD_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "words.txt")
MAX_SLICES = 6  # total lives

def main():
    print("Welcome to Save the Watermelon!")  # greet player
    
    # load all words from file
    words = load_words(WORD_FILE)
    
    # pick one secret word randomly
    secret_word = choose_word(words)
    
    guessed_letters = []  # list of letters player guessed
    slices_left = MAX_SLICES  # start with max slices
    
    # game loop
    while slices_left > 0 and not is_win(secret_word, guessed_letters):
        print("\nWord:", render_word(secret_word, guessed_letters))  # show current word
        print(f"Slices left: {slices_left}")  # show remaining lives
        
        guess = input("Guess a letter: ").lower()  # get letter from player
        
        # check if input is valid
        if not guess.isalpha() or len(guess) != 1:
            print("Please type a single letter!")  # invalid input
            continue
        
        if guess in guessed_letters:
            print("You already guessed that!")  # repeated guess
            continue
        
        guessed_letters.append(guess)  # add to guessed list
        
        # check if guess is in secret word
        if guess in secret_word:
            print("Nice! You got a letter!")  # correct guess
        else:
            slices_left -= 1  # lose a slice
            print(f"Wrong! The watermelon got sliced. ({slices_left} slices left)")
    
    # end of game messages
    if is_win(secret_word, guessed_letters):
        print(f"Congratulations! You saved the watermelon! The word was '{secret_word}'.")
    else:
        print(f"Oh no! The watermelon was sliced. The word was '{secret_word}'.")
    
    # ask if player wants to play again
    replay = input("Play again? (y/n): ").lower()
    if replay == 'y':
        main()  # restart game
    else:
        print("Thanks for playing!")

# only run the game if this file is executed directly
if __name__ == "__main__":
    main()