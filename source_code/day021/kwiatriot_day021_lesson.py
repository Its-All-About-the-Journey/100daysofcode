"""
Day 021 of the 100 Days of Code course
Author: Wayne Kwiat
Date: 1/23/2021
"""
# Class inheritance

# Initial class created
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

# Class modeled off the base class - Adding the Super class into the ()
class Fish(Animal):
    def __init__(self):
        # The following adds all features from super class and initializes it into new object
        super().__init__()

    # This is a modified version of the super class for the new class
    def breathe(self):
        # Below initializes the object with the super class method and then adds the class specifics
        super().breathe()
        print("doing this underwater")

    def swim(self):
        print("moving in water.")


nemo = Fish()
nemo.swim()
nemo.breathe()

