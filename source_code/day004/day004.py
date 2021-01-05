import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

move = ['rock', 'paper', 'scissors']
graphic = [rock, paper, scissors]
flag = 'y'

while flag in ['y', 'yes']:

	player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
	if player not in [0, 1, 2]:
		print("Invalid selection. Try again...")
		continue
	print('\n', graphic[player])
	player = move[player]

	comp = random.choice([0, 1, 2])
	print(f'Computer chose:\n{graphic[comp]}')
	comp = move[comp]

	if (player == 'rock' and comp == 'paper') or (player == 'paper' and comp == 'scissors') or (player == 'scissors' and comp == 'rock'):
		print('You lose')
	elif player == comp:
		print('You tied. Choose again...\n')
		continue
	else:
		print('You win!')

	flag = input('Play Again (Y/N)?').lower()

