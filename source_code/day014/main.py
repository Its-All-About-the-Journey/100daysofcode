from art import logo, vs
from game_data import data
import random



def options():
  choice_a = random.choice(list(data))
  choice_b = random.choice(list(data))
  while choice_a == choice_b:
    choice_b = random.choice(list(data))
  return choice_a, choice_b

def print_round(choice_a, choice_b):
  print(f"Compare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}")
  print(vs)
  print(f"Against B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}")

def decision(choice_a, choice_b):
  user_pick = str.lower(input(f"Who has more followers? Type 'A' or 'B': \n"))
  if user_pick == 'a' and choice_a['follower_count'] > choice_b['follower_count']:
    return True
  elif user_pick == 'a' and choice_a['follower_count'] < choice_b['follower_count']:
    return False
  elif user_pick == 'b' and choice_b['follower_count'] > choice_a['follower_count']:
    return True
  else:
    return False
    
def round():
  # print the logo
  print(logo)

  # randomly pick two options from data
  choice_a, choice_b = options()

  # print the two options
  print_round(choice_a, choice_b)

  # Have the user make a decision and go through the logic
  outcome = decision(choice_a, choice_b)
  return outcome

score = 0

winning = True
while winning == True:
  outcome = round()
  if outcome == True:
    print("That is correct!\n")
    score += 1
    print(f"Your current score = {score}")
  else:
    print("That is incorrect.\n")
    print(f"Your final score = {score}.")
    winning = False
