# words.py

# This file handles the word list for the game

# Function to get all words from a file
def get_words(file_path):
    """Return a list of words from the given file"""
    words = []
    with open(file_path, 'r') as f:  # open the file for reading
        for line in f:
            word = line.strip()  # remove newline and spaces
            if word:  # ignore empty lines
                words.append(word)  # add word to list
    return words  # return the full list

# Function to add a new word to the file
def add_word(file_path, new_word):
    """Add a new word to the file"""
    new_word = new_word.strip().lower()  # clean it up
    with open(file_path, 'a') as f:  # open file in append mode
        f.write(new_word + '\n')  # write the new word on a new line

# Function to check if a word is already in the list
def word_exists(file_path, word):
    """Check if the word is already in the file"""
    words = get_words(file_path)  # get all words
    return word.lower() in words  # return True if exists
