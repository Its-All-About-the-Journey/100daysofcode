# 100 Days of Code: Python
# Utility Library
# @hypermanganate

import os

# Clear screen
def clear_screen():
  """
  Execute system call to clear the screen.
  """
  if os.name == "posix":
    os.system('clear')
  else:
    os.system('cls')

# Yes or No Choice
def yes_or_no():
  """
  Prompt Yes or No and return True or False
  """
  choice = None

  while True:
    try:
      while choice not in ['y', 'n', 'yes', 'no']:
        choice = input("Please choose yes or no: ")
      break
    except ValueError:
      print("Please enter yes or no only.")
      continue

  if choice in ['y', 'yes']:
    return True

  return False

# A or B Choice
def a_or_b(choice_a, choice_b):
  """
  Prompt to choose between two string values.

  Return the selected value.

  """
  choice = None

  # This should throw an exception if the supplied value cannot be cast as string.
  func_choice_a = str(choice_a).lower()
  func_choice_b = str(choice_b).lower()

  while True:
    try:
      while choice not in [func_choice_a, func_choice_b]:
        choice = input(f"""Choose {func_choice_a} or {func_choice_b}: """)
      break
    except ValueError:
      print(f"""Please enter {func_choice_a} or {func_choice_b} only.""")
      continue

  if choice == func_choice_a:
    return choice_a

  return choice_b
