import random

question = input("Choose betwen Heads or Tails?").capitalize()

toss = random.randint(0, 1)

if question == "Heads":
    if toss == 1:
        print("Heads, you win!")
    else:
        print("Tails.. You loss!")
        
elif question == "Tails":
    if toss == 0:
        print("Tails, you win!")
    else:
        print("Heads.. You loss!")