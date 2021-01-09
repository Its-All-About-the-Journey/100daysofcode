import random
#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
word_list_len = (len(word_list) - 1)
chosen_word = word_list[random.randint(0, word_list_len)]
#print(chosen_word)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
letter = input("Please, guess a letter: ").lower()
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for char in chosen_word:
    if char == letter:
        print(f"{letter} = {char} Correct!")
    else:
        print("Wrong")