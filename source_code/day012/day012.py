# Grant Armstrong
# 01/15/2021
# Day 12 Number Guessing Game


from art import logo
from random import randint


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
number = randint(1, 100)

# print(f"Pssst, the correct answer is {number}")

# Validate selection of game difficulty
while True:
	difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
	if difficulty in ['easy', 'hard']:
		break
	else:
		print("Invalid difficulty selection. Please try again...")

# Set number of guesses
guesses = 10 if difficulty == 'easy' else 5

# Loop that handles game execution
while True:
	# Print remaining guesses and request new guess
	print(f"You have {guesses} attempts remaining to guess the number.")
	player_guess = int(input("Make a guess: "))

	# Exit game if player has no guesses left
	if not guesses:
		exit()
	# Print winning message and exit if player guesses correctly
	elif player_guess == number:
		print(f"You got it! The answer was {number}")
		exit()

	# Print high/low based on player guess
	if player_guess > number:
		print("Too high.")
	elif player_guess < number:
		print("Too low.")

	# Subtract a guess and print either "Guess Again" or tell the player they've lost
	guesses -= 1
	print("Guess again." if guesses != 0 else "You've run out of guesses, you lose")
	continue

