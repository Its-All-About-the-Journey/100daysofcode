# 8.1
# -----------------------------------------------
def one():
    # Review: 
    # Create a function called greet(). 
    # Write 3 print statements inside the function.
    # Call the greet() function and run your code.

    def greet():
        print("a")
        print("b")
        print("c")

    greet()

    def greet_name(name):
        print(f"hello {name}")

    greet_name("anthony")

    def greet_with(name, location):
        greet_name(name)
        print(f"what's is like in {location}")

    greet_with("anthony", "minneapolis")

# 8.2
# -----------------------------------------------
def two():
    #Write your code below this line 👇
    from math import ceil
    def paint_calc(height, width, cover):
        print(f"You'll need {ceil(height * width / cover)} cans of paint.")

    #Write your code above this line 👆
    # Define a function called paint_calc() so that the code below works.   

    # 🚨 Don't change the code below 👇
    test_h = int(input("Height of wall: "))
    test_w = int(input("Width of wall: "))
    coverage = 5
    paint_calc(height=test_h, width=test_w, cover=coverage)

# 8.3
# -----------------------------------------------
def three():
    import math
    def prime_checker(number):
        for i in range(2, math.isqrt(number) + 1):
            if number % i == 0:
                print("It's not a prime number.")
                return
        print("It's a prime number.")