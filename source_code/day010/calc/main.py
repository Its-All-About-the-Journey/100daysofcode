from art import logo

print(logo)

# calculator

#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    num1 = float(input("What's the first number?: "))
    # num2 = int(input("What's the second number?: "))

    print("Calculator options:")
    for i in operations:
        print(i)

    keep_going = True

    while keep_going:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the second number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation or type 'q' to quit: ").lower()
        if choice == "y":    
            num1 = answer      
        elif choice == "n":
            keep_going = False
            calculator()
        else:
            break

calculator()

