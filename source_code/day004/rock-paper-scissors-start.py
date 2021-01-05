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
import random

your_choice = input("What do you choose.\n - Type 0 for Rock.\n - Type 1 for Paper.\n - Type 2 for Scissors.\nAnswer: ")
choice_int = int(your_choice)
print("====================================")
print("Your Choise is:")
if choice_int == 0:
    print(rock)
elif choice_int == 1:
    print(paper)
else:
    print(scissors)
print("====================================")
print("PC Choise is:")
pc_choice = random.randint(0,2)
if pc_choice == 0:
    print(rock)
elif pc_choice == 1:
    print(paper)
else:
    print(scissors)
print("====================================")
#user = Piedra, papel, tijera
#pc = Piedra, papel, tijera
row1 = ["Tied", "Won", "Lost"]
row2 = ["Lost", "Tied", "Won"]
row3 = ["Won", "Lost", "Tied"]
mapping = [row1, row2, row3]
print(mapping[pc_choice][choice_int])
print(f"++++++++++++++++++++")
print(f"++++++++++++++++++++    You {mapping[pc_choice][choice_int]} !!")
print(f"++++++++++++++++++++")
