#!/usr/bin/env python3
# 100 Days of Code : Day 14 Project
# Higher Lower Game
# Adam Pawlowski (@hypermanganate)

from game_data import data
from art import logo, vs
from hundred_days_util import a_or_b, yes_or_no, clear_screen
from random import randint

# Const

# Decl

high_score = 0

# Func

def get_competitor(game_data_list):
  """
  Return a random dict of competitor data from the game data list.
  Take advantage of the mutability of a list that I'd just learned about.
  """

  if not len(game_data_list):
    return False
  else:
    return game_data_list.pop(randint(0, len(game_data_list) - 1))

def setup(data):
  """
  Setup values for a new game.
  """

  game_data_list = data[:]
  game_score = 0

  return game_data_list, game_score

def print_display(a, b, game_score):
  """
  Print the Higher or Lower Game Display
  """

  clear_screen()
  print(logo)
  if game_score:
    print(f"""You're right! Current score: {game_score}.""")
#  print(f"""Compare A: {a['name']}, {a['description']}, from {a['country']} ({a['follower_count']}).""")
  print(f"""Compare A: {a['name']}, {a['description']}, from {a['country']}.""")
  print(vs)
#  print(f"""Compare B: {b['name']}, {b['description']}, from {b['country']} ({b['follower_count']}).""")
  print(f"""Compare B: {b['name']}, {b['description']}, from {b['country']}.""")

def get_selection():
  """
  Obtain and return the user's choice.
  """

  print("Who has more followers?", end=' ')
  selection = a_or_b("A", "B")

  return selection

def get_winner(a, b):
  """
  Return True if the combatant beats the champion.
  """

  if b['follower_count'] > a['follower_count']:
    return True

  return False

def do_lost_game(game_score):
  """
  Player has lost the game, display game over screen.
  """

  clear_screen()
  print(f"""Sorry, that's not correct. Your score was: {game_score}""")

def game(game_data_list, game_score, champion = None):
  """
  Main Game Loop
  """

  if not len(game_data_list):
    clear_screen()
    print(logo)
    print("Conglaturation, Your Winner!")
    return False, game_score, None

  if not champion:
    champion = get_competitor(game_data_list)
  correct = False
  combatant = get_competitor(game_data_list)
  print_display(champion, combatant, game_score)
  winner = get_winner(champion, combatant)
  selection = get_selection()

  if selection == "A" and not winner:
    correct = True
    champion = combatant
  elif selection == "B" and winner:
    correct = True
    champion = combatant

  if not correct:
    do_lost_game(game_score)
    return False, game_score, champion
  else:
    game_score += 1
    return True, game_score, champion

if __name__ == '__main__':
  if not len(data) >= 2:
    print("Error, insufficient game data.")
    exit()

  while True:
    game_data_list, game_score = setup(data)
    game_state = True
    champion = None
    while game_state:
      game_state, game_score, champion = game(game_data_list, game_score, champion)
    if game_score > high_score:
      high_score = game_score
      print("You've got the high score!")
    print(f"""High score is currently {high_score}""")
    print("Would you like to play again?", end=' ')
    if not yes_or_no():
      break
