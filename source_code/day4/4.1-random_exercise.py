#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲

# You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
# Important, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.

# There are many ways of doing this. 
# But to practice what we learnt in the last lesson, you should generate a random number, either 0 or 1. 
# Then use that number to print out Heads or Tails.

# 1 means Heads
# 0 means Tails

import random

coin_toss = input("Would you like to flip a coin? Yes or No? ").lower()
random_integer = random.randint(0, 1)

if coin_toss == "yes":
    print("Flipping the coin.")
    print("The coin is flipping in the air!")
    print("Fingers crossed &.")
    if random_integer == 1:
        print("Heads! You Win the coin toss!")
        choice = input("Do you want to kick or receive the football? Kick or Recieve? ").lower()
        if choice == "kick":
            print("You have opted to kick the ball.")
        else:
            print("You have opted to recieve the ball.")
    else:
        print("Tails, You Lose!")
else:
    print("Oops, I fat fingered it.")

random_side = random.randint(0, 1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")

