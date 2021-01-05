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
images = [rock, paper, scissors]

print("Let's play a game of Rock, Paper, Scissors!")
user_choice = int(input("Type 0 for Rock, 1 for Paper, and 2 for Sissors.\nWhat is your choice: "))
if user_choice >= 3 or user_choice < 0:
    print("Number out of range, you lose!")
else:
    print(images[user_choice])

    comp_choice = random.randint(0, 2)
    print("Computer chose:")
    print(images[comp_choice])

    if user_choice == 0 and comp_choice == 2:
        print("You win!")
    elif comp_choice == 0 and user_choice == 2:
        print("You lose")
    elif comp_choice > user_choice:
        print("You lose")
    elif user_choice > comp_choice:
        print("You win!")
    elif user_choice == comp_choice:
        print("Its a draw!")
