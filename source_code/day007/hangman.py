#Step 5
import os
import platform
sysos = platform.platform()
import random
import hangman_art
import hangman_words

end_of_game = False
win = False
lives = 6
chosen_word = ""
testing = 0

if sysos[0] == "Windows":
  os.system('cls')
else:
  os.system('clear')
#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo + "\n")

try:
  difficulty = int(input("\nSelect the word length you would like (4-10) or enter for random: "))
except ValueError:
  difficulty = 0
if sysos[0] == "Windows":
  os.system('cls')
else:
  os.system('clear')
print(hangman_art.logo + "\n")
shuffledwordlist = hangman_words.word_list
random.shuffle(shuffledwordlist)
chosen_words_bylen = [x for x in shuffledwordlist if len(x) == difficulty]

if difficulty >=4 and difficulty <= 10:
  chosen_word = random.choice(chosen_words_bylen)
else:
  chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
#Testing code
if testing == 1:
  print(f'Pssst, the solution is {chosen_word}.\n')
#Tell the user how many letters they chose (this is also here just to keep the formatting consistent):
print(f"\n\nYou chose a word with {word_length} letters.")
print(hangman_art.stages[lives])
#Create blanks
display = []
for _ in range(word_length):
    display += "_"
prior_guesses = []
print(f"{' '.join(display)}")
while not end_of_game:
    guess = input("\nGuess a letter: ").lower()
    if sysos[0] == "Windows":
      os.system('cls')
    else:
      os.system('clear')
    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in prior_guesses:
      print(hangman_art.logo + "\n")
      #Testing code
      if testing == 1:
        print(f'Pssst, the solution is {chosen_word}.\n')
      print(f"Letters guessed: {prior_guesses}")
      print(f"\nYou've already guessed {guess}, please guess a different letter.")
      print(hangman_art.stages[lives])
      print(f"{' '.join(display)}")
    else:
      prior_guesses += guess
    #Check guessed letter
      for position in range(word_length):
          letter = chosen_word[position]
          if letter == guess:
              display[position] = letter
      #TODO-3: - Import the logo from hangman_art.py and print it at the start of the game. 
      print(hangman_art.logo + "\n")
      #Testing code
      if testing == 1:
        print(f'Pssst, the solution is {chosen_word}.\n')
      print(f"Letters guessed: {prior_guesses}")
	  
      #Check if user is wrong.
      if guess not in chosen_word:
          lives -= 1
          if lives == 0:
            end_of_game = True
            print(f"\nYou've been hung.  The word was: {chosen_word}")
          else:
            print(f"\n'{guess}', is not a letter in the word, you're one step closer to hanging.")
      elif "_" not in display:
        end_of_game = True
        print("\nYou win!  There won't be a hanging today!")
      else:
        print(f"\nYou got a letter! {guess}")

      print(hangman_art.stages[lives])

      print(f"{' '.join(display)}")
