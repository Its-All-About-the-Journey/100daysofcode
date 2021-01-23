# 🚨 Simple Functions 👇
def greet():
  print("Hello Robin")
  print("How do you do Bre?")
  print("Isn't the weather nice today?")
greet()

# 🚨 Function that allows for input 👇
#'name is the parameter.
#'Robin is the argument
def greet_with_name(name):
  print(f"Hello {name}")
  print(f"How do you do {name}")
greet_with_name("Robin")

# 🚨 Functions with more than 1 input 👇
def greet_with(name, location):
    print(f"Hello {name}.")
    print(f"What is it like in {location}?")

#Calling greet_with() with Positional Arguments
greet_with("Robin", "New York")
#vs.
greet_with("New York", "Robin")

#Calling greet_with() with Keyword Arguments
greet_with(location="New York", name="Robin")