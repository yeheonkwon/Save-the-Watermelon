# test_logic.py

# import functions from logic.py
from src.logic import render_word, is_win

# Test if render_word works correctly
def test_render_word():
    secret = "apple"  # the word to guess
    guessed = ["a", "p"]  # letters guessed so far
    result = render_word(secret, guessed)  # get the display
    # check if it matches expected output
    assert result == "a p p _ _", f"Expected 'a p p _ _', got {result}"

# Test if is_win returns True when all letters are guessed
def test_is_win():
    secret = "apple"
    guessed = ["a", "p", "l", "e"]
    assert is_win(secret, guessed) == True, "Expected True"

# Test if is_win returns False when not all letters are guessed
def test_is_not_win():
    secret = "apple"
    guessed = ["a", "p", "l"]
    assert is_win(secret, guessed) == False, "Expected False"

# Run tests manually
if __name__ == "__main__":
    test_render_word()  # run first test
    test_is_win()       # run second test
    test_is_not_win()   # run third test
    print("All tests passed!")  # success message
