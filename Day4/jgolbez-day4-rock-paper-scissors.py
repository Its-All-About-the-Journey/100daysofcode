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

rps_choices = [rock, paper, scissors]

player_choice = int(input("What will you choose? 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
if player_choice >= 3 or player_choice < 0:
  print("You picked an invalid choice! You lose!")
else: 
  print("Player Choice:\n")
  print(rps_choices[player_choice])
  computer_choice = rps_choices[random.randint(0, 2)]
  print("Computer Choice:\n")
  print(computer_choice)

  if rps_choices[player_choice] == computer_choice:
    print("Game is a Draw")
  elif rps_choices[player_choice] == rock:
    if computer_choice == scissors:
      print("Player wins!")
    else:
      print("Player loses!")
  elif rps_choices[player_choice] == scissors:
    if computer_choice == paper:
      print("Player wins!")
    else:
      print("Player loses!")
  else:
    if computer_choice == rock:
      print("Player wins!")
    else:
      print("Player loses!")
