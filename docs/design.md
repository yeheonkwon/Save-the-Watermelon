\# Save the Watermelon - Design



\## Game Rules

\- Player guesses letters to save the watermelon.

\- Each wrong guess costs a slice.

\- Win if all letters are guessed before slices run out.

\- Lose if slices reach zero.



\## Game Flow

1\. Start the game.

2\. Pick a random secret word.

3\. Show masked word (e.g., \_ a \_ e).

4\. Ask player to guess a letter.

5\. If guess is correct, reveal letters.

6\. If guess is wrong, decrease slices.

7\. Repeat steps 4-6 until win or lose.

8\. Show win/lose message.



\## Data Structure

\- `secret\\\_word` : string, the word to guess

\- `guessed\\\_letters` : list, letters the player has guessed

\- `slices` : integer, remaining lives

