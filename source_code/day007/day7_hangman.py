import random
import os
from hagman_word import word_list
from hagman_art import logo
from hagman_art import stages

chosen_word = random.choice(word_list)

print(logo)
lives = 6

display = []
word = len(chosen_word)
for char in range(word):
    display += "_"
print(f"{' '.join(display)}")

dead = False
while not dead:
    guess = input("Guess a letter: ").lower()
    os.system('clear')
    print(logo)
    for letter in range(word):
        letters = chosen_word[letter]
        if letters == guess:
            display[letter] = letters

    print(stages[lives])
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            dead = True
            print("You don't have live anymore!\nYou are dead!")
            print(stages[lives])
    if "_" not in display:
        dead = True
        print("You Win!")
