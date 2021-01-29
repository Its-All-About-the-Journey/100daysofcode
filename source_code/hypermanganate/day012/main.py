#!/usr/bin/env python3
# 100 Days of Code : Day 12 Project
# Number Guessing Game
# Adam Pawlowski (@hypermanganate)

import random
from art import logo
from hundred_days_util import clear_screen, a_or_b

# Const

EASY_GUESSES = 10
HARD_GUESSES = 5

# Func

# Get Target Number
def get_target_number():
  """
  Return a random number between 1 and 100 for the computer's guess
  """

  guess = random.randint(1,100)

  return guess

# Print Remaining Guesses
def print_guesses_remaining():
  """
  Prints the remaining guesses.
  """

  print(f"""You have {number_guesses_remaining} attempts remaining to guess the number.""")

# Get Guess
def get_guess():
  """
  Get the guess from the player.
  """

  guess = None

  # Obtain a guess, and filter out non integer guess, outside of the range.
  while True:
    try:
      while not guess in range(1, 101):
        guess = int(input("Make a guess: "))
      break
    except ValueError: # Wasn't an int
      print("Enter a number between 1 and 100, please.")
      continue

  return guess

# Check Guess
def check_guess(guess):
  """
  Ascertain if the guess supplied is higher or lower than the computer's guess (target_number).
  Return a value indicive of one of the three possible states.
  """
  if guess > target_number: # Higher
    return 1
  if guess < target_number: # Lower
    return -1

  return 0 # Just Right

# Opening Greeting
def greeting():
  """
  Game's opening text, instructions, and difficulty level selection.
  """

  print("""Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.""")
  print("Choose a difficulty.", end = ' ') # No newline so the choice is adjoined.

  difficulty = a_or_b("easy", "hard")  # Library function to assist in choice.

  return difficulty

# Main

clear_screen()
print(logo)

number_guesses_remaining = 0

# Setup the game
target_number = get_target_number()
difficulty = greeting()

# Set the number of guessss
if difficulty == "easy":
  number_guesses_remaining = EASY_GUESSES
else:
  number_guesses_remaining = HARD_GUESSES

# While we have guesses remaining
while number_guesses_remaining:
# Should stop on 0 evaluating to false.
  print_guesses_remaining()
  player_guess = get_guess()
  result = check_guess(player_guess) # Check the guess against the target
  if not result:
    print(f"""That's it! The number was {player_guess}! You win!""")
    exit()
  elif result > 0:
    print("Too high, guess again.")
  else:
    print("Too low, guess again.")
  number_guesses_remaining -= 1
