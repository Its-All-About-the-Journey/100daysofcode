"""
Day 011 of the 100 Days of Code course
Author: Wayne Kwiat
Date: 1/11/2021

A Number guessing game
"""

import random
import sys

logo = """
   ______                        __  __            _   __                __             
  / ____/_  _____  __________   / /_/ /_  ___     / | / /_  ______ ___  / /_  ___  _____
 / / __/ / / / _ \/ ___/ ___/  / __/ __ \/ _ \   /  |/ / / / / __ `__ \/ __ \/ _ \/ ___/
/ /_/ / /_/ /  __(__  |__  )  / /_/ / / /  __/  / /|  / /_/ / / / / / / /_/ /  __/ /    
\____/\__,_/\___/____/____/   \__/_/ /_/\___/  /_/ |_/\__,_/_/ /_/ /_/_.___/\___/_/                                                                                            
"""
print(logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty level. Type 'easy' or 'hard': ")
# Choosing the difficulty level
if difficulty == "easy":
    number_of_guesses = 10
    print(f"You have {number_of_guesses} attempts remaining to guess the number.")
else:
    number_of_guesses = 5
    print(f"You have {number_of_guesses} remaining to guess the number.")
# Choosing the random number between 1 and 100
number = random.randint(1, 100)
print(number)

while number_of_guesses > 0:
    number_of_guesses -= 1
    guess = int(input("Make a guess: "))
    if guess == number:
        print(f"You win, the number was {number}.")
        sys.exit(0)
    elif guess < number:
        print("Too low.")
    elif guess > number:
        print("Too high.")

    if number_of_guesses == 0:
        print(f"You loose, the number was {number}")
        sys.exit(0)

    print("Guess again.")
    print(f"You have {number_of_guesses} remaining to guess the number.")

