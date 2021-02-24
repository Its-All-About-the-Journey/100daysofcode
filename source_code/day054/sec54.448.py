def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1/n2


# First-class objects: can be passed around as arguments
def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)

result = calculate(add, 2, 3)
print(result)


# Nested function
def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    return nested_function


inner_function = outer_function()
inner_function()