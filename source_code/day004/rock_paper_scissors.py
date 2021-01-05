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

user_choice = int(input(
    "What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

pc_choice = random.randint(0, 2)

signs = [rock, paper, scissors]

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    if (user_choice == 0 and pc_choice == 2) or (user_choice == 1 and pc_choice == 0) or (user_choice == 2 and pc_choice == 1):
        print(signs[user_choice])
        print("Computer chose:")
        print(signs[pc_choice])
        print("You win!")
    else:
        print(signs[user_choice])
        print("Computer chose:")
        print(signs[pc_choice])
        print("You lose.")
