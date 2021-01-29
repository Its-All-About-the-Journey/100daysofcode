#!/usr/bin/env python3
# 100 Days of Code : Day 6 Project
# Reeborg Maze Solver
# Adam Pawlowski (@hypermanganate)

import random
from hangman_words import word_list
from hangman_art import stages, logo
from string import ascii_lowercase

def draw_display(display, lives):
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    print(stages[lives])

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
remaining_letters = list(ascii_lowercase)

house_rule = False # Penalty on repeat guess
play_for_real = False # Reveal the word before you play
end_of_game = False
lives = 6

print(logo + '\n')

if input("Are we playing for real? (y) ").lower() == "y":
  play_for_real = True

if input("\nHouse Rule: Penalty on Repeat Guess (y) ").lower() == "y":
  house_rule = True

print("\n")

#Testing code
if not play_for_real:
    print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = ['_']
display *= len(chosen_word)

# Guesses
# I want to track guesses, both good and bad.
guesses = []

while not end_of_game:
    print("Your choices:")
    print(' '.join(remaining_letters))
    guess = input(f"""({lives} lives remaining) Guess a letter: """).lower()
    if guess in guesses:
      print(f"""You've already guessed {guess}!""")
      if house_rule:
        lives -= 1
        draw_display(display, lives)
        if lives == 0:
            end_of_game = True
            print("You lose.")
      continue
    else:
       guesses.append(guess)
       remaining_letters.remove(guess)

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"""Sorry, {guess} was not in the word.""")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"""You lose. The word was {chosen_word}.""")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    draw_display(display, lives)
