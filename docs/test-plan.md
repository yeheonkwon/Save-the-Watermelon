# Save the Watermelon - Test Plan

## Why We Test
We just want to make sure the game works like it's supposed to. This plan checks if guesses, slices, wins, and losses all work fine.

## Test Cases

1. **Guess a Correct Letter**
   - Do this: Type a letter that is in the secret word.
   - Should happen: The letter shows up in the word display.

2. **Guess a Wrong Letter**
   - Do this: Type a letter that is NOT in the word.
   - Should happen: You lose a slice. Game shows how many slices are left.

3. **Guess the Same Letter Again**
   - Do this: Type a letter you already guessed.
   - Should happen: Game says "You already guessed that letter!" and asks for a new input.

4. **Type Something Invalid**
   - Do this: Type a number, symbol, or more than one letter.
   - Should happen: Game says "Invalid input!" and asks again.

5. **Winning the Game**
   - Do this: Guess all letters correctly before slices run out.
   - Should happen: Game says "You saved the watermelon!" and ends.

6. **Losing the Game**
   - Do this: Keep guessing wrong letters until slices reach 0.
   - Should happen: Game says "The watermelon got sliced!" and shows the word.

7. **Edge Case**
   - Do this: Only 1 slice left, then guess wrong.
   - Should happen: Game ends properly and shows the losing message.

## Example Play

1. Start game → word: "apple"  
2. Guess "a" → shows  
3. Guess "x" → slices decrease  
4. Guess "p" → shows  
5. Guess "l" → shows  
6. Guess "e" → shows  
7. Game shows: "You saved the watermelon!"  

## Notes
- Test all of this manually in the console.  
- Only letters should be accepted.  
- Keep track of slices after wrong guesses.  
- This plan covers normal play and tricky situations.

## How to Run & Record Results
1. Open terminal / command prompt.  
2. Run the game: `python -m src.game`  
3. Follow steps in Example Play and Test Cases.  
4. Write down results or take screenshots to show the game behaves correctly.
