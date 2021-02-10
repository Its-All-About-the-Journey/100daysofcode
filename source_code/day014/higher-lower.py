import art
from game_data import data
import random
from os import system

def logo():
    system('cls')
    print(art.logo)

def choices():
    return random.choices(data, k=2)

#comparisons = random.choices(data, k=2)
score = 0

logo()
while True:
    comparisons = choices()
    print(f"{comparisons[0]['name']}\n{art.vs}\n{comparisons[1]['name']}")
    guess = 0 if input("Who has more followers? Type 'A' or 'B': ").upper() == 'A' else 1
    if comparisons[guess]['follower_count'] > comparisons[1 if guess == 0 else 0]['follower_count']:
        #comparisons[0] = comparisons[guess]
        score += 1
        logo()
        print(f"You're right! Current score: {score}.")
        #comparisons[0 if guess == 1 else 0] = random.choice(data)
    else: break

print(f"Sorry, that's wrong. Final score: {score}")