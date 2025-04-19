import random 

with open("possible_words.txt","r",encoding="utf-8") as f: 
    possible_words = (f.read().split("\n")) 
    
possible_words.sort() 
random_word = possible_words[random.randint(0,len(possible_words))] 
#print(random_word) # Uncomment to see the random word

# Function that displays the result of a guess
def display_guess_result(guess): 
    output = ["","","","",""] 
    letters = list()
    
    for idx, letter in enumerate(guess): 
        output[idx] = "\u200A" + letter.capitalize() + "\u200A" 

    for letter in random_word: 
        letters.append(letter) 

    for idx, letter in enumerate(guess): 
        if letter == random_word[idx]: 
            output[idx] = '\x1b[5;30;42m\u200A' + letter.capitalize() + '\u200A\x1b[0m' # Green for correct position
            letters.remove(letter) 

    for idx, letter in enumerate(guess): 
        # This ensures that double letters are displayed correctly
        if letter in random_word and letter in letters: 
            if "[5;30;42m" not in output[idx]: # Check if letter is already green so it doesn't get changed to yellow
                output[idx] = '\x1b[6;30;43m\u200A' + letter.capitalize() + '\u200A\x1b[0m' # Yellow for wrong position
                letters.remove(letter) 

    print(("\u200A".join(output))) 

with open("possible_guesses.txt","r",encoding="utf-8") as f:
    possible_guesses = (f.read().split("\n"))

# Recursive function that checks user guess and calls the display function
def make_guess(guesses_left = 6):
    user_guess = input()
    if user_guess in possible_guesses:
        guesses_left -= 1
        display_guess_result(user_guess)
        if user_guess == random_word:
            print(f'Success!\nYou got it in {6-guesses_left} tries')
            exit()
        elif guesses_left == 0:
            print(f"Fail :(\nThe word was: {random_word}")
        else:
            make_guess(guesses_left)
    elif user_guess == "quit": # Allow user to quit the game
        print(f"The word was {random_word}")
        exit()
    else:
        print("Not a valid word")
        make_guess(guesses_left)

print("Input 5 letter word:")
make_guess()