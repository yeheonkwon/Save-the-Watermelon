\# Save the Watermelon - Pseudocode



\## Main Game Loop

FUNCTION main\_game\_loop

&nbsp;   # 1. Load all words from the word list

&nbsp;   words ← load\_words\_from\_file()



&nbsp;   # 2. Pick one random word as the secret word

&nbsp;   secret\_word ← pick\_random\_word(words)



&nbsp;   # 3. Prepare guessed letters list and slices (lives)

&nbsp;   guessed\_letters ← empty list

&nbsp;   slices ← set\_number\_based\_on\_word\_length(secret\_word)



&nbsp;   # 4. Repeat until player wins or runs out of slices

&nbsp;   WHILE slices > 0 AND word\_not\_fully\_guessed(secret\_word, guessed\_letters)

&nbsp;       # 4a. Show current word state with guessed letters

&nbsp;       DISPLAY render\_word(secret\_word, guessed\_letters)



&nbsp;       # 4b. Ask the player to input one letter

&nbsp;       guess ← ask\_player\_for\_letter(guessed\_letters)



&nbsp;       # 4c. Check if letter is already guessed

&nbsp;       IF guess is already in guessed\_letters THEN

&nbsp;           DISPLAY "You already guessed that letter!"

&nbsp;       ELSE

&nbsp;           # 4d. Add guess to guessed letters

&nbsp;           add guess to guessed\_letters



&nbsp;           # 4e. Check if guess is in the secret word

&nbsp;           IF guess is in secret\_word THEN

&nbsp;               DISPLAY "Nice! You found a letter."

&nbsp;           ELSE

&nbsp;               decrease slices by 1

&nbsp;               DISPLAY "Wrong! Slice lost. Remaining slices: " + slices

&nbsp;   END WHILE



&nbsp;   # 5. Game over: win or lose message

&nbsp;   IF word\_not\_fully\_guessed(secret\_word, guessed\_letters) is FALSE THEN

&nbsp;       DISPLAY "You saved the watermelon!"

&nbsp;   ELSE

&nbsp;       DISPLAY "Oh no! The watermelon got sliced."

&nbsp;       DISPLAY "The word was: " + secret\_word

END FUNCTION



