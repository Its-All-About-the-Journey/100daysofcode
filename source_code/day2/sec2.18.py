# len() gives an error when provided a number instead of a string
# len(4387) = TypeError: object of type 'int' has no len()

# TypeError: can only concatenate str (not "int") to str
num_char = len(input("What is your name: "))
print("Your name has " + num_char + " characters.")

# <class 'int'>
print(type(num_char))
print(type(len(input("What is your name: "))))

# Type Conversation or Type Casting
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

# Integer
a = 123
print(type(a))

# Convert Integer to a string
a = str(123)
print(type(a))

# Convert integer to a float
a = float(123)
print(type(a))

# <class 'float'> convert string to float
print(70 + float("100.5"))

# Converts integers to strings and concatenates
print(str(70)+ str(100))