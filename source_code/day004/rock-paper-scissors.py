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

options = [rock, paper, scissors]

while True:
    try:
        choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
        if choice < 3 and choice >= 0:
            break
        else:
            print("You typed an invalid number!")
    except:
        print("You typed an invalid number!")

computer_choice = random.randint(0,2)

print(options[choice])
print(f"Computer chose:\n{options[computer_choice]}")

if choice == computer_choice:
    print("Tie!")
elif choice == 0 and computer_choice == 1 or choice == 1 and computer_choice == 2 or choice == 2 and computer_choice == 0:
    print("You lose")
else:
    print("You win!")
