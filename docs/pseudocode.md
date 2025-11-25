# Save the Watermelon - Pseudocode

## Main Game Loop  
```
FUNCTION main_game_loop  
    # 1. Load all words from the word list
    words ← load_words_from_file()

    # 2. Pick one random word as the secret word
    secret_word ← pick_random_word(words)

    # 3. Prepare guessed letters list and slices (lives)
    guessed_letters ← empty list
    slices ← set_number_based_on_word_length(secret_word)

    # 4. Repeat until player wins or runs out of slices
    WHILE slices > 0 AND word_not_fully_guessed(secret_word, guessed_letters)
        # 4a. Show current word state with guessed letters
        DISPLAY render_word(secret_word, guessed_letters)

        # 4b. Ask the player to input one letter
        guess ← ask_player_for_letter(guessed_letters)

        # 4c. Check if letter is already guessed
        IF guess is already in guessed_letters THEN
            DISPLAY "You already guessed that letter!"
        ELSE
            # 4d. Add guess to guessed letters
            add guess to guessed_letters

            # 4e. Check if guess is in the secret word
            IF guess is in secret_word THEN
                DISPLAY "Nice! You found a letter."
            ELSE
                decrease slices by 1
                DISPLAY "Oops! Slice lost. Remaining slices: " + slices
    END WHILE

    # 5. Game over: win or lose message
    IF word_not_fully_guessed(secret_word, guessed_letters) is FALSE THEN
        DISPLAY "You saved the watermelon!"
    ELSE
        DISPLAY "Oh no! The watermelon got sliced."
        DISPLAY "The word was: " + secret_word
END FUNCTION
```
