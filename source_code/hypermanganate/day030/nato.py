# 100 Days of Code: Python
# Day 26
# NATO Wordulator
# Adam Pawlowski (@hypermanganate)

import pandas

# Load DataFrame from CSV file
nato_df = pandas.read_csv('./nato_phonetic_alphabet.csv')

# Create Dict of NATO Letter:Code
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}

# Setup
print("NATO Wordulator\n")

trying = True

while trying:

    # Get User Word
    user_word = input("What word do you need to decode? ")

    # Compute Output

    try:

        print("Your NATO word is: " +
              f"{str.join(' ', [nato_dict[letter.upper()] for letter in user_word])}")

        break

    except KeyError:
        print("It's SNAFU! You entered a word containing something"
              + " other than letters A-Z. It's all FUBAR!")
