#!/usr/bin/env python3
# 100 Days of Code : Day 15 Project
# Coffee Machine
# Adam Pawlowski (@hypermanganate)

from data import coin_values, machine_actions, prices, recipe, resources

# Func

def collect_money():
  """
  Collect money from the user and make sure the values are acceptable.
  
  Returns False on bad input.
  Returns the value inserted into the machine otherwise.
  """

  print("Give me your money")
  coin_tray = {}
  
  try:
    for coin in coin_values:
      coin_tray[coin] = int(input(f"""How many {coin}?: """))
      if coin_tray[coin] < 0:
        print("Tilt")
        return False
  except ValueError:
    return False

  inserted_value = 0.0

  for coin in coin_tray:
    inserted_value += coin_values[coin] * coin_tray[coin]

  return inserted_value


def sufficient_resources(coffee):
  """
  Validate sufficient resources are available to make the requested beverage.

  Returns True if sufficient resources, otherwise False.
  """

  for ingredient in recipe[coffee]:
    if resources[ingredient]['value'] < recipe[coffee][ingredient]:
      print(f"""Sorry, there is not enough {ingredient}.""")
      return False

  return True

def subtract_resources(coffee):
  """
  Subtract the resources needed for the coffee from the machine's resources.

  Always returns True.
  """

  for ingredient in recipe[coffee]:
    resources[ingredient]['value'] -= recipe[coffee][ingredient]
  
  return True

def make_coffee(coffee):
  """
  A general coffee making function.

  Ensures there are enough resources, collect coins, and give change.
  Finally, subtract the resources and pass back the process as successful with True.

  If there was a problem with coinage, we fall through with False back to the main loop so the application can proceed.

  """
  if not sufficient_resources(coffee):
    return False
  
  print(f"""{coffee.capitalize()} costs ${prices[coffee]:.2f}""")
  
  coin_in = collect_money()
  if coin_in:
    # Money has been inserted.
    change = coin_in - prices[coffee]
    if change < 0:
      print("Insufficent funds.")
      return False
    if change > 0:
      print(f"""Here is ${round(change,2):.2f} in change.""")

    resources['Money']['value'] += prices[coffee]

    subtract_resources(coffee)

    return True
  else:
    # They couldn't hande inserting coins. No coffee.
    return False
  
def print_report():
  """
  Print a report of the machine's resources.
  """

  print(f"""Coffee Machine Supply Status:""")
  for resource in resources:
    if resource != "Money":
      print(f"""* {resource}: {resources[resource]['value']}{resources[resource]['unit']}""")
    else:
      print(f"""* {resource}: ${resources[resource]['value']:.2f}""")

def prompt_for_action():
  """
  Prompt the user to choose a machine action.

  Returns the choice.
  """

  choice = None

  while choice not in machine_actions:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

  return choice

def do_coffee_loop():
  """
  Repeat endlessly asking the user to make a choice, until the loop is broken by turning the machine off.
  """
  while True:
    action = prompt_for_action()
    if action == "off":
      break
    elif action == "report":
      print_report()
    else:
      # A cup of coffee has been requested
      if make_coffee(action):
        print(f"""Here is your {action} ☕. Enjoy!""")
      else:
        print(f"""Unable to make {action}.""")

  return

# Main

if __name__ == '__main__':
      do_coffee_loop()
