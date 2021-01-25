#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_number(guess, answer, turns):
    if guess > answer:
        print("Is too high")
        return turns - 1
    elif guess < answer:
        print("Is too low")
        return turns - 1
    else:
        print(f"You got it!! The answer is: {answer}")

def difficulty():
    global turns
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
        
def game():
    print(logo)
    print("Welcome to the guessing game!")
    print("I'm thinking of a number between 1 and 100...")
    answer = randint(1,100)
    turns = difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} turns left")
        guess = int(input("Guess a number: "))
        turns = check_number(guess,answer, turns)
        if turns == 0:
            print("You ran out of guesses, sorry.")
            return
game()