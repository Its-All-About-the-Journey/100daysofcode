
# DAY 17

OOP Quiz Game

# Description

An object-oriented style of quiz game, in that the code is object oriented.

PEP8 insists that code lines not be so long because of people using ancient terminals or something and I got sick of wrapping everything around.
I also skipped the copy and paste more data, though the example sets the stage for using an API later.

# Environment
OS: Ubuntu Bionic

Python version: 3.8.7

# Dependencies

Quiz Brain
Question Model
Data File

# How to run script
```
Call main.py and play up to 12 questions of riviting trivia.
```

# Sample output
```
Question #1: A few ounces of chocolate can to kill a small dog. (True/False)? t
That's right!
The correct answer was: True.
Your current score is 1/1

Question #2: No piece of square dry paper can be folded in half more than 7 times. (True/False)? true
That's wrong!
The correct answer was: False.
Your current score is 1/2

Question #3: Approximately one quarter of human bones are in the feet. (True/False)? false
That's wrong!
The correct answer was: True.
Your current score is 1/3

...

Question #12: A slug's blood is green. (True/False)? f
That's wrong!
The correct answer was: True.
Your current score is 4/12
Game over! Your score was: 4/12
```

# Other Exercises

## Social Media User Class Example

```
class User:
    def __init__(self, user_id: int, username: str) -> 'User':
        super().__init__()
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, followed_user):
        self.following += 1
        followed_user.followers += 1

    def report(self):
        print(f"""User {self.id} has {self.followers} followers, and is following {self.following}.""")


user_1 = User("1", "fart")
user_2 = User("2", "burp")

user_1.report()
user_2.report()
user_1.follow(user_2)
user_1.report()
user_2.report
```

