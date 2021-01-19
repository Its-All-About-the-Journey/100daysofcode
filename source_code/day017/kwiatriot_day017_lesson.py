"""
Day 017 of the 100 Days of Code course
Author: Wayne Kwiat
Date: 1/18/2021
"""

# Introduction into creating classes
# Class names use Pascal Case (Every first letter capitalized)
class User:
    # This is the function to initialize attributes of classes, must be passed in at creation
    def __init__(self, user_id, user_name):
        # This is the attribute 'id' and is accessed by "object name".id
        self.id = user_id
        # This is the attribute 'user_name and is accessed by "object name".user_name
        self.user_name = user_name
        # This is a default attributes
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


# Here we are creating objects of the User class and passing in the needed values
user_1 = User("001", "Wayne")
user_2 = User("002", "Marta")
user_1.follow(user_2)

print(user_1.id)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

