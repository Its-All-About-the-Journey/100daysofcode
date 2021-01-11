import os
import random

from art import logo

# Clear the terminal screen
def clear() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def update_calc_screen(key_pressed=0):
    clear()
    print( logo.format(key_pressed) )

def get_num(msg):
    return float( input(msg) )

def get_op(msg, operations):
    for op in operations:
        print(op)
    
    return input(msg)

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


update_calc_screen()

num1 = get_num("What's the first number?: ")
update_calc_screen(num1)

more_operations = True

while more_operations:

    op = get_op('Pick an operation from the line above: ', operations)
    update_calc_screen(op)

    num2 = get_num("What's the next number? ")
    
    answer = operations[op](num1, num2)
    print(f'{num1} {op} {num2} = {answer}')
    update_calc_screen(answer)
 
    next_step = input(f"Type 'y' to continue with {num1}, 'r' to restart, or 'n' to exit.: ")

    if next_step == 'y':  # Continue
        num1 = answer

    elif next_step == 'r': # Restart
        update_calc_screen()
        num1 = get_num("What's the first number?: ")

    else: # Exit
        for _ in range(1000):
            update_calc_screen(random.randint(0,99999999999999999))
            print('You broke the calculator!!!')
        
        more_operations = False
