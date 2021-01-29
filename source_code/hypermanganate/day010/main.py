#!/usr/bin/env python3
# 100 Days of Code : Day 10 Project
# Calculator
# Adam Pawlowski (@hypermanganate)

from art import print_logo

operations = ['+', '-', '*', '/']

# Arithmetic Operations

# Addition
def add(value1, value2):
  """
  Add two values and return the result
  """
  if type(value1) not in [int, float] or type(value2) not in [int, float]:
    raise ValueError
  else:
    return value1 + value2

# Subtraction
def sub(value1, value2):
  """
  Subtract value 2 from value 1 and return the result
  """
  if type(value1) not in [int, float] or type(value2) not in [int, float]:
    raise ValueError
  else:
    return value1 - value2

# Multiplication
def mult(value1, value2):
  """
  Multiply two values and return the result
  """
  if type(value1) not in [int, float] or type(value2) not in [int, float]:
    raise ValueError
  else:
    return value1 * value2

# Division
def div(value1, value2):
  """
  Divide value one by value two and return the result
  """
  if type(value1) not in [int, float] or type(value2) not in [int, float]:
    raise ValueError
  else:
    return value1 / value2

# Calculator Functions

# Get User Operation Selection
def get_operation():
  """
  Prompt the user to select a valid operation, and return the user's selection
  """
  operation = None
  while not operation in operations:
    print(f"""Operations: {' '.join(operations)}""")
    operation = input("Pick an operation: ")

  return operations.index(operation)

# Perform Arithmetic
def do_math(val1, val2, operand):
  """
  Do a requested calculation with two values given.
  """
  if operand < 1:
    return add(val1,val2)
  if operand < 2:
    return sub(val1,val2)
  if operand > 2:
    return div(val1,val2)

  return mult(val1,val2)

# Determine Continuance
def get_continue_choice(result):
  """
  Prompt the user to continue calculating if desired.
  """
  choice = None
  while choice not in ['y', 'n', 'q']:
    choice = input(f"""Type 'y' to continue calculating with {result}, type 'n' to start a new calculation, or 'q' to quit: """).lower()
  if choice == "y":
    return result
  elif choice == "q":
     exit()
  else:
    return None

# Main Application Loop
def do_calculator(memory):
  """
  Calculator application operational loop.
  """
  if not memory:

    try:

      memory = float(input("What's the first number?: "))

    except ValueError:

      print("Invalid entry, try again.")
      return None

  else:

    print(f"""The first number is: {memory}""")

  operation = get_operation()
  try:

    operand = float(input("What's the next number?: "))

  except ValueError:

    print("Invalid entry, try again.")
    return memory

  result = do_math(memory, operand, operation)

  print(f"""{memory} {operations[operation]} {operand} = {result}""")
  memory = get_continue_choice(result)

  return memory

# Main
memory = None

while True:
  print_logo(memory)
  memory = do_calculator(memory)
