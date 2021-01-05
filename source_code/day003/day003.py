print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice = input('You\'re at a cross road. Where do you want to go? Type "left" or "right"\n')
if choice.lower() != 'left':
	print('You have fallen into a hole. Game Over.')
	exit()
else:
	choice = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. '
	               'Type "swim" to swim across\n')
	if choice.lower() != 'wait':
		print('You have been attacked by a trout. Game Over.')
		exit()
	else:
		choice = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one '
		               'blue. Which colour do you choose?\n')
		if choice.lower() == 'red':
			print('You have been burned by fire. Game Over.')
			exit()
		elif choice.lower() == 'blue':
			print('You have been eaten by beasts. Game Over.')
			exit()
		elif choice.lower() != 'yellow':
			print('Invalid choice. You have died. Game Over.')
			exit()
		else:
			print('You Win!')

