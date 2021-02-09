from art import logo
import random
chosen_number = random.randint(1, 100)
print(f"{logo}\n\nWelcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nChoose a difficulty. Type 'easy' or 'hard': ")
attempts = 10 if input() == 'easy' else 5
while (attempts := attempts - 1) > -1:
    guess = int(input("Make a guess: "))
    if guess != chosen_number and attempts > 0: print(f"Too high. Guess again\nYou have {attempts} remaining attempts to guess the number." if guess > chosen_number else f"Too low. Guess again\nYou have {attempts} remaining attempts to guess the number.")
    else: break
print(f"You are out of guesses! The answer was {chosen_number}" if attempts == 0 else f"You got it! The answer was {chosen_number}")