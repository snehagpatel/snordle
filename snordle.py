import string
import csv
import random as randpy
import enchant
from nltk.corpus import words


### Define variables for the loop of the game
# d --> the dictionary for checking word validity
# ans --> randomly selected snordle
# answer_list --> list of possible snordles
# game_on --> dictates whether the game will continue
# alph --> set of the alphabet lowercased (used to validate inputs)
# attempts --> number of attempts the user has to guess the snordle
# last_result --> last result given to user after submitting a guess

d = enchant.Dict("en_US")
ans = ""
answer_list = [x for x in words.words() if x.isalpha() and len(x) == 5 and \
    x[:2] == 'sn' and d.check(x)] + ["sneha"]
game_on = True
alph = set(string.ascii_uppercase)
attempts = 6
last_result = ""

# randomly pick ans from list of words
def start_game():
    global answer_list
    global ans
    global game_on
    global attempts
    
    # get answer list and randomly picks an answer for the current wordle
    #answer_list = [row['Word'] for row in file]
    ans = (randpy.choice(answer_list)).upper()
    game_on = True
    attempts = 6
    return


#   Requests input of snordle guess from player
#   Outputs the string input if valid 
def get_guess():
    global game_on
    global ans
    global attempts
    global d
    word = input("Type in your word guess (" + str(attempts) + \
        " guesses remaining): ").upper().strip()
    while(True):
        if word == "ESC":
            game_on = False
            break
        elif not word.isalpha():
            print("ERR: Input must be letters only.")
            word = input("Enter valid guess: ").upper().strip()
            print()
        elif len(word) != len(ans):
            print("ERR: Input must be " + str(len(ans)) + " letters long.")
            word = input("Enter valid guess: ").upper().strip()
            print()
        elif not d.check(word) and word != "SNEHA":
            print("ERR: Input must be a valid word")
            word = input("Enter valid guess: ").upper().strip()
            print()
        else:
            break
    attempts = attempts - 1
    return word

#   Compares answer to guess 
#   Outputs a string that represents how close they are
def compare_guess(answer, guess):
    i = 0
    result = ""
    container = answer
    for c in guess:
        if answer[i] == c:
            result += c
            container = container.replace(c, "", 1)
            #print(container)
        elif c in container:
            if c not in guess[i+1:]:
                result += "(" + c + ")"
            else:
                result += "_"
        else:
            result += "_"
        i += 1
    return result

# reads result, and if the correct word, returns True and ends game
def game_won(result):
    global ans
    global game_on
    if ans == result:
        game_on = False
        print("You won! The Snordle was " + ans)
        return True
    return False

# checks if the game has been lost
def game_lost():
    global ans
    global attempts
    global game_on
    global last_result
    if attempts == 0:
        game_on = False
        if game_won(last_result):
            return False
        print("You have run out of guesses. The Snordle was " + ans)
        return True
    return False






### Gameplay

print("Welcome to Snordle: a sneha-made Wordle!")
print('To play, type "play". For instructions on how to play, type "help".\n')



  
while True:
    inp = input("What would you like to do?\nType here: ").upper().strip()
    if inp == "PEEPEE":
        print("POOPOO!")
    elif inp == "POOPOO":
        print("PEEPEE!")
    elif inp == "HELP":
        print("TODO: put instructions here :D")
    elif inp == "PLAY":
        playing = True
        while playing:
            print("\nStarting game...")
            start_game()
            print("Word has been selected!")
            while game_on:
                last_result = compare_guess(ans, get_guess())
                if game_on:
                    print(last_result)
                    game_won(last_result)
                    game_lost()
            replay = input('Thanks for playing! Press "q" to quit, or any other key to play again.').upper().strip()
            if replay == 'Q':
                playing = False
    elif inp == "QUIT":
        break
    








    