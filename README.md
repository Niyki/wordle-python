# wordle-python
Super short python CLI that let's you play wordle.

## How to use
Running the code will promt the user to input a 5 letter word. Users have 6 attempts to guess the word; invalid attempts (e.g., inputting a word not found in _possible_guesses.txt_) will not reduce attempts remaining. Letters that are in the word and in the correct position will be highlighted in **green**. Letters that are in the word but in the incorrect position will be highlighted in yellow.

The possible words that can be selected as the wordle can be edited in _possible_words.txt_.

The possible guesses that count as valid words can be edited in _possible_guesses.txt_.
