#Step 5
import os
import platform
sysos = platform.platform()
import random
import hangman_art
import hangman_words

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo + "\n")
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
prior_guesses = []
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if sysos[0] == "Windows":
      os.system('cls')
    else:
      os.system('clear')

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in prior_guesses:
      print(hangman_art.logo + "\n")
      print(f"You've already guessed {guess}, please guess a different letter.")
      #Testing code
      print(f'Pssst, the solution is {chosen_word}.')
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
      print(f'Pssst, the solution is {chosen_word}.')
      
      #Check if user is wrong.
      if guess not in chosen_word:
          print(f"'{guess}', is not a letter in the word, you lose a life.")
          lives -= 1
          if lives == 0:
              end_of_game = True
              print("You lose.")
  
      #Check if user has got all letters.
      if "_" not in display:
          end_of_game = True
          print("You win.")
           
      print(hangman_art.stages[lives])
      #Join all the elements in the list and turn it into a String.
      print(f"{' '.join(display)}")

