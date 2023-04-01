import art
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


print(art.logo)

num1 = int(input("What's the first number?: "))

for oper in operations:
  print(oper)
operation_symbol = input("Pick an operation from the line above: ")
num2 = int(input("What's the second number?: "))

prev_answer = operations[operation_symbol](num1, num2)
print (f"{num1} {operation_symbol} {num2} = {prev_answer}")
user_go = input("Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ")
while user_go == "y":
  operation_symbol = input("Pick another opeation: ")
  nextnum = int(input("What's the next number?: "))
  new_answer = operations[operation_symbol](prev_answer, nextnum)
  print (f"{prev_answer} {operation_symbol} {nextnum} = {new_answer}")
  user_go = input(f"Type 'y' to continue calculating with {new_answer}, or type 'n' to exit.: ")
  prev_answer = new_answer