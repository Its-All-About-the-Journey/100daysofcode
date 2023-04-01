import art
import time
from replit import clear
#Add:
def add(n1, n2):
  return n1 + n2
#Subtract:
def subtract(n1, n2):
  return n1 - n2
#Multiply:
def multiply(n1, n2):
  return n1 * n2
#Divide:
def divide(n1, n2):
  return n1 / n2

#Error check user input and require a good value:
def get_number(prompt_text):
  """Enter the prompt text you want to see as the input and function will loop until valid value is entered."""
  while True:
    try:
      return float(input(prompt_text))
      break
    except ValueError:
      print("Bad value, try again", end='\r')
      time.sleep(1)
      print("                    ", end='\r')
      print("\x1b[1A", end='\r')
################################################
def get_oper(prompt_text):
  """Enter the prompt text you want to see as the input and function will loop until valid operator is entered."""
  while True:
    operation_symbol = input(prompt_text)
    if operation_symbol in operations:
      return operation_symbol
      break
    else:
      print("Bad value, try again", end='\r')
      time.sleep(1)
      print("                    ", end='\r')
      print("\x1b[1A", end='\r')
#################################################
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculator():
  print(art.logo)
  num1 = get_number("\rWhat's the first number?: ")
  all_oper = []
  for oper in operations:
    all_oper.append(oper)
  print(f"Possible operations: {all_oper}")
  cont = True
  while cont == True:
    operation_symbol = get_oper(f"Pick an operation for: {num1} ")
    num2 = get_number(f"Give the next number for: {num1} {operation_symbol} ")
    answer = operations[operation_symbol](num1, num2)
    print (f"{num1} {operation_symbol} {num2} = {answer}")
    user_choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
    if user_choice == "y":
      num1 = answer
    elif user_choice == "n":
      cont = False
      clear()
      calculator()
    else:
      cont = False


calculator()