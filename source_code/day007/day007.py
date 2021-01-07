import random
import termcolor
import art
import words


word_list = words.word_list
chosen = random.choice(word_list).lower()
display_word = list('_' * len(chosen))  # Easier method of creating the display word _ _ _ _ format
lives = 7
guess_list = []
allowed_characters = 'abcdefghijklmnopqrstuvwxyz'

print(art.logo)

while '_' in display_word and lives > 0:
	# Display initial hangman display
	print(art.stages[lives])
	# Print as much of the word as the player has guessed
	print(' '.join(display_word), '\n')
	# Display the characters the player has already guessed, but only if he's already made a guess
	print(f"So far, you have guessed the following letter(s): {', '.join(guess_list)}\n" if guess_list else '')
	# Ask for the guess
	guess = input("Guess a letter: ").lower()
	# Run some validation to ensure it was a single letter entered - restart loop if input isn't valid
	if len(guess) != 1 or guess not in allowed_characters:
		print(termcolor.colored('Your guess must be a single letter!', 'red'))
		continue
	# If the player chooses a character they've already guessed, tell them and restart loop
	if guess in guess_list:
		print(termcolor.colored(f'You have already guessed "{guess}"...', 'yellow'))
		continue
	# Run a for loop on the enumeration of the chosen word (similar to using range(chosen) but easier)
	for i, char in enumerate(chosen):
		# What happens if guess isn't in word
		if guess not in chosen:
			print(termcolor.colored(f'"{guess}" is not found in the word!\n', 'red'))
			# Add the word to the already guessed list, if it isn't already in there
			if guess not in guess_list:
				guess_list.append(guess)
			# Subtract a life since they guessed wrong
			lives -= 1
			# Break out of the for loop because there's no need to continue testing conditions
			break
		# What happens if guess is in word
		elif guess == char:
			# Use if statement so message only printed 1x even if letter found > 1 in the word
			if guess not in guess_list:
				print(termcolor.colored(f'"{guess}" is found in the word!\n', 'green'))
			# Fill in display word with the guess character
			display_word[i] = guess
			# Add the guess character to the guess list if it doesn't already exist in it
			if guess not in guess_list:
				guess_list.append(guess)

# Final printout of winning/losing message with fancy coloring
if lives == 0:
	lose_word = termcolor.colored(chosen, 'green', 'on_red')
	print(f'{art.stages[lives]}\n The word was {lose_word}... You have been hung. Sorry for your loss.')
else:
	win_word = termcolor.colored(chosen, 'red', 'on_green')
	print(f'{win_word} is correct! You WIN!')





