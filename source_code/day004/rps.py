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

your_input = input("What do your choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: \n")

#Convert your choice from string to int
your_choice = int(your_input)

#Computer chooses
computer_choice = random.randint(0,2)

#Print ASCII Art for Your Choice
if your_choice == 0:
  print(rock)
if your_choice == 1:
  print(paper)
if your_choice == 2:
  print(scissors)

#Print a divider
print("*" * 10 + "COMPUTER CHOOSES" + "*" * 10)

#Print ASCII Art for Computer Choice
if computer_choice == 0:
  print(rock)
if computer_choice == 1:
  print(paper)
if computer_choice == 2:
  print(scissors) 

#Game Logic
if your_choice == 0 and computer_choice == 1:
  print("Paper covers rock - YOU LOSE!")
elif your_choice == 0 and computer_choice == 2:
  print("Rock beats Scissors - YOU WIN!")
elif your_choice == 1 and computer_choice == 0:
  print("Paper covers rock - YOU WIN!")
elif your_choice == 1 and computer_choice == 2:
  print("Scissors cuts paper - YOU LOSE!")
elif your_choice == 2 and computer_choice == 0:
  print("Rock cruches scissors - YOU LOSE!")
elif your_choice == 2 and computer_choice == 1:
  print("Scissors cuts paper - YOU WIN!")
elif your_choice == computer_choice:
  print("IT\'S A TIE!")
else:
    print("You typed an invalid number!")