import art

def operation():
    for operator in operations:
        print(operator)
    return input("Pick an operation: ")

def calculate(number1, number2, operator):
    current_result = eval(f"{number1}{operator}{number2}")
    print(f'{number1} {operator} {number2} = {current_result}')
    return current_result

operations = ["+", "-", "*", "/"]

print(art.logo)

while True:
    answer = calculate(number1=float(input("What's the first number?: ")), operator=operation(), number2=float(input("What's the next number?: ")))
    while input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower() == "y":
        answer = calculate(answer, operator=operation(), number2=float(input("What's the next number?: ")))