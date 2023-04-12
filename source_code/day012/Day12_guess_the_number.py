#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random

print(logo)
print("I'm thinking of a number between 1 and 100.")

mynum = random.randint(1,100)

if input("Choose a difficulty. Type 'easy' or 'hard': ") == "easy":
  turns = 10
  print(f"You have {turns} attempts remaining to guess the number.")
else:
  turns = 5

while turns > 0:
  guess = int(input("Make a guess: "))
  if guess == mynum:
    print("You guessed the number! You Win!")
    break
  elif guess > mynum:
    print("Too high.")
    turns -= 1
    print(f"You have {turns} attempts remaining to guess the number.")
  elif guess < mynum:
    print("Too low.")
    turns -= 1
    print(f"You have {turns} attempts remaining to guess the number.")
if turns == 0:
  print("No more guesses, you loose.")