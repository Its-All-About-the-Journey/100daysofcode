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

hand = [rock, paper, scissors]
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user >= 3 or user < 0:
    print("Not a good number, you lose!")
else:
    print(f"You did:\n {hand[user]}")
    computer = random.randint(0, 2)
    print(f"Computer did:\n{hand[computer]}")

    if user == 0 and computer == 2:
        print("You wins!")
    elif computer == 0 and user == 2:
        print("Computer Wins!")
    elif computer > user:
        print("Computer Wins!")
    elif user > computer:
        print("You win!")
    elif computer == user:
        print("Egality!")
