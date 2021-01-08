"""
Day 007 of the 100 Days of Code course
Author: Wayne Kwiat
Date: 1/7/2021
"""

import random
import hangman_art
import hangman_words


word_list = hangman_words.word_list
# Choosing a random word from the world list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
# Setting the game status and lives
end_of_game = False
lives = 6

logo = hangman_art.logo
print(logo)
# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# Create blanks for the display wordlist
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You already guessed {guess}.")
    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that is not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])