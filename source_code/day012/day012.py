# Grant Armstrong
# 01/15/2021
# Day 12 Number Guessing Game

from art import logo
import random


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
number = random.randint(1, 100)
print(f"Pssst, the correct answer is {number}")

while True:
	difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
	if difficulty in ['easy', 'hard']:
		break
	else:
		print("Invalid difficulty selection. Please try again...")

guesses = 10 if difficulty == 'easy' else 5


while True:
	if guesses == 0:
		print("You've run out of guesses, you lose")
		exit()
	else:
		print("Guess again.")
	print(f"You have {guesses} attempts remaining to guess the number.")
	player_guess = int(input("Make a guess: "))
	if player_guess > number:
		print("Too high.")
		guesses -= 1
		continue
	elif player_guess < number:
		print("Too low.")
		guesses -= 1
		continue
	elif player_guess == number:
		print(f"You got it! The answer was {number}")
		exit()
