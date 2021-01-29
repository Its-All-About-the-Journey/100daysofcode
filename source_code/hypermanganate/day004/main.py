#!/usr/bin/env python3
# 100 Days of Code : Day 4 Project
# Rock Paper Scissors
# Adam Pawlowski (@hypermanganate)

# 0 = Rock, 1 = Paper, 2 = Scissors
import random

def print_scorecard(scores):

  print(f"""
  ****************************
  * | Player  | | Computer | *
  * ----------- ------------ *
  *    {"{:3d}".format(scores[0])}          {"{:3d}".format(scores[1])}      *
  ****************************
  """)

def solve_game(player_choice, computer_choice):
  outcomes = [[0,0,1],[1,0,0],[0,1,0]]
  return outcomes[player_choice][computer_choice]

def print_game_board(player_text, computer_text):
  print(f"""You choose {player_text}:""")
  print(globals()[player_text])
  print(f"""Computer chooses {computer_text}:""")
  print(globals()[computer_text])
  print(f"""You chose {player_text}, and computer chose {computer_text}.\n""")

def get_choices():

  print("Rock Paper Scissors")
  while True:
    try:
      player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors (Enter to quit): "))
      if player_choice not in choices and player_choice != '':
        raise
      elif player_choice == '':
        exit()
      break
    except:
      print("Invalid selection, try again.")
      continue
  computer_choice = random.randint(0,2)

  return player_choice, computer_choice

##

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

choices = [0,1,2]
text_choices = ["rock","paper","scissors"]
scores = [0,0]

# Main

while True:

  player_choice, computer_choice = get_choices()

  player_text = text_choices[player_choice]
  computer_text = text_choices[computer_choice]

  print_game_board(player_text, computer_text)

  if solve_game(player_choice, computer_choice):
    print(f""""{player_text.capitalize()} beats {computer_text}!"\nYou Win!""")
    scores[0] += 1
  else:
    print(f"""{player_text.capitalize()} loses to {computer_text}. Sorry, you lose.""")
    scores[1] += 1

  print_scorecard(scores)

  if input("""Play again? (y) """).lower() != "y": break
  print("\n\n\n")

"""
 C 0   1   2
p

0  0L -1L -2W

1  1W  0L -1L

2  2L  1W  0L
"""

# I wrote this, but then realized they're considering a matrix here for this exercise:

#if player_choice > 0 and player_choice - computer_choice == 1:
#  print("Win")
#elif player_choice == 0 and player_choice - computer_choice == -2:
#  print("Win")
#else:
#  print("Lose")

# Another win emssage
#print("You win!") if outcomes[player_choice][computer_choice] else print("You lose!")
