#Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')


num_chars = len(chosen_word)

# Creating list of _
display = ( '_ ' * num_chars ).split()

# Create a list version of the chosen word
chosen_word_list = list(chosen_word)

while display != chosen_word_list:
    # Get user input
    guess = input("Guess a letter: ").lower()

    # If guess matches, replace _ with guessed letter
    for index in range(num_chars):
        if guess.lower() == chosen_word[index]:
            display[index] = guess.lower()

    # Update display
    print('='*80)
    print(display)
    print('='*80)
