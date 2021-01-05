import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock,paper,scissors]

row1 = ["draw", "lose", "win"]
row2 = ["win", "draw", "lose"]
row3 = ["lose", "win","draw"]
outcome = [row1,row2,row3]

compChoice = random.randint(0,2)
playerChoice = int(input("Choose a 0 for Scissors, 1 for Rock and 2 for Paper:\n"))

#grid = [compChoice-1,playerChoice-1]

print(f"You choose: \n{options[playerChoice]} \nThe computer choose: \n{options[compChoice]}")
print(f"\nYou {outcome[playerChoice-1][compChoice-1]}.")