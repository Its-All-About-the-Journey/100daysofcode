import art
from game_data import data
import random
from os import system
score = 0
system('cls')
print(art.logo)
comparisons = random.sample(data, k=2)
while True:
    print(f"{comparisons[0]['name']}, a {comparisons[0]['description']}, from {comparisons[0]['country']}\n{art.vs}\n{comparisons[1]['name']}, a {comparisons[1]['description']}, from {comparisons[1]['country']}")
    guess = 0 if input("Who has more followers? Type 'A' or 'B': ").upper() == 'A' else 1
    if comparisons[guess]['follower_count'] > comparisons[1 if guess == 0 else 0]['follower_count']:
        score += 1
        system('cls')
        comparisons[0] = comparisons[1]
        comparisons[1] = random.choice([x for x in data if x != comparisons[0]]) 
        print(f"{art.logo}\nYou're right! Current score: {score}.")
    else: break
print(f"Sorry, that's wrong. Final score: {score}")