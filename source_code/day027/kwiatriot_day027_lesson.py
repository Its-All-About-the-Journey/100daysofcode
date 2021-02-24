"""
Day 027 of the 100 Days of Code course
Author: Wayne Kwiat
Date: 2/6/2021
"""

# Many positional arguments with the *(came be any name) traditionally args
# Creates arguments as a tuple
def add(*args):
    num_sum = 0
    for n in args:
        num_sum += n
    return num_sum


print(add(1, 2, 3))

# Many keyword arguments with the **(can be any name) traditionally kwargs
# Creates arguments as a dictionary
def calculate(n, **kwargs):
    # how to iterate through a dictionary
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kwargs):
        # the get() method allows these to be optional arguments when called
        self.model = kwargs.get("model")
        self.make = kwargs.get("make")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")


my_car = Car(make="Nissan", model="Pathfinder")
print(my_car.model)
# If no parameter is passed then it returns none
print(my_car.seats)
