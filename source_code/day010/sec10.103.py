from art import logo


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

more_operations = True

num1 = int(input("What's the first number?: "))
 
while more_operations:

    for op in operations:
        print(op)

    op = input('Pick an operation from the line above: ')
    num2 = int(input("What's the next number? "))
    
    answer = operations[op](num1, num2)
    print(f'{num1} {op} {num2} = {answer}')
    
    num1 = answer

    more_operations = input(f"Type 'y' to continue with {num1}, or type 'n to exit.: ") == 'y'