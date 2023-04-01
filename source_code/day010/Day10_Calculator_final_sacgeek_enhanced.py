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
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}
all_oper = []
for oper in operations:
  all_oper.append(oper)
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

def calculator():
  print(art.logo)
  print("Enter your math equation as, 'number' ENTER, 'operator' ENTER, 'number' ENTER")
  print(f"Possible operations: {all_oper}")
  cont = True
  again = False
  while cont == True:
    if again == False:
      num1 = get_number("Num1: ")
    oper = get_oper("Oper: ")
    num2 = get_number("Num2: ")
    answer = operations[oper](num1, num2)
    print(answer)
    user_choice = input("Press 'y' to continue, 'c' to clear and start over, or ENTER to end. ")
    if user_choice == "y":
      num1 = answer
      again = True
      print("\x1b[1A" + "                                                                                         ", end='\r')
      print("\x1b[1A" + "                                                                                         ", end='\r')
      print("\x1b[1A" + "                                                                                         ", end='\r')
      print("\x1b[1A" + "                                                                                         ", end='\r')
      print("\x1b[1A" + "                                                                                         ", end='\r')
      print(f"num1: {answer}")
    elif user_choice == "c":
      cont = False
      clear()
      calculator()
    else:
      cont = False
calculator()