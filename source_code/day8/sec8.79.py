# 🚨 Functions 👇

# def my_function(something):
#   Do this with something
#   Then do this
#   Finally do this

# my_function(123)

# something within def function is called "Parameter"
# 123 within my_function call is called "Argument"

# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
    print("Hello")
    print("My Name is Robin")
    print("What is your name?")

greet()

# 🚨 Function that allows for input 👇
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}")

greet_with_name("Robin")