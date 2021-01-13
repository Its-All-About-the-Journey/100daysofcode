import random

print("Welcome to the Number Guessing Game!")

print("I'm thinking of a number between 1 and 100.")

difficultyChoice = input("Choose a difficulty. Type 'easy' or 'hard': \n")

choicesLeft = 0
if difficultyChoice == "easy":
    choicesLeft = 10
else:
    choicesLeft = 5

def choices_left_print(choicesLeft):
    print(f"You have {choicesLeft} attempts remaining to guess the number")

choices_left_print(choicesLeft)
answer = random.choice(range(1, 100))
guessIncorrect = True

while guessIncorrect:
    guess = int(input("Make a guess: "))
    if guess < 1 or guess > 100:
        print("Invalid number")
    elif guess < answer:
        choicesLeft -= 1
        print("Too low")
        choices_left_print(choicesLeft)
    elif guess > answer:
        choicesLeft -= 1
        print("Too high")
        choices_left_print(choicesLeft)
    elif guess == answer:
        print("Correct choice! You win.")
        guessIncorrect = False
    else:
        print("Invalid choice")
    if choicesLeft == 0:
        print("You have no choices left, you lose.")
        guessIncorrect = False



