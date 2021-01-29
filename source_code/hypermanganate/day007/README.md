# DAY 7

Hangman

# Description

A Hangman game.

If I'd had more time/effort for this, I'd have made a "difficulty" selector, instead of turning off the word preview.
I would assign the difficulties like:
 Easy: 50% Reveal
 Medium: 25% Reveal
 Hard: (Default) 0% Reveal

Then get a value for the number of letters in the chosen word this represents, rounding down.
Select random letters up to that amount, and place them into position in the display.

# Environment
OS: Ubuntu Bionic

Python version: 3.6.9

# Dependencies

None

# How to run script
```
Simply call the script.

Choose if you'd like to play for real, or if you'd like to practice (at hangman) by seeing the solution early.

Choose if you'd like the House Rule, to accept a penalty for a repeated guess.

Then, play hangman.

```

# Sample output
```

 _
| |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |
                   |___/

Are we playing for real? (y) y

House Rule: Penalty on Repeat Guess (y) n


Your choices:
a b c d e f g h i j k l m n o p q r s t u v w x y z
(6 lives remaining) Guess a letter: q
Sorry, q was not in the word.
_ _ _ _ _

  +---+
  |   |
  O   |
      |
      |
      |
=========

Your choices:
a b c d e f g h i j k l m n o p r s t u v w x y z
(5 lives remaining) Guess a letter: l
Sorry, l was not in the word.
_ _ _ _ _

  +---+
  |   |
  O   |
  |   |
      |
      |
=========

Your choices:
a b c d e f g h i j k m n o p r s t u v w x y z
(4 lives remaining) Guess a letter:
```

# Other Exercises

# Step One

See if the user has guessed correctly

```
from random import choice

#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = choice(word_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("User, supply your guess: ").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

if guess in chosen_word:
  print("Congratulations, you have passed this test.")
else: 
  print("You have angered the computer with your inaccurate guess.")
```

# Step TWo

Update the display

```
#Step 2

from random import choice
word_list = ["aardvark", "baboon", "camel"]
chosen_word = choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = ['_']
display *= len(chosen_word)
guess = input("Guess a letter: ").lower()

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

# I spent a moment here trying to do something with .index(), but this only gives the first value. You can specify a starting index, but, then you'd have to store that.
# I also learned about _ , so chosen_word.index(guess) , if it were '1', makes _ = 1 until you change it. I thought I could be slick with it. 
# In the end I ended up searching Snack Overload and ended up with enumerate, which I'd seen before to run an iterator along side another function.
# I was also trying to not change the code that was there before and word around it, which wasn't going to happen. I could put a scan inside the if/true branch, but that seemed wasteful.

for i, letter in enumerate(chosen_word):
    if letter == guess:
        print("Right")
        display[i] = guess
    else:
        print("Wrong")

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
print(display)
```

# Step Three

Know when you've won

```
while '_' in display:

  guess = input("Guess a letter: ").lower()

  #Check guessed letter
  for position in range(word_length):
      letter = chosen_word[position]
      print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
      if letter == guess:
          display[position] = letter

  print(display)

print("Your Winner")
```

# Step Four

Keep Track of Lives

```
while not end_of_game:
    guess = input(f"({lives} lives remaining) Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
      lives -= 1
      if lives < 1: end_of_game = True

    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])

print("No lives remaining. You've lost.")
```

