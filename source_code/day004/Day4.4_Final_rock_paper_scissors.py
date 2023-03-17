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

#Write your code below this line 👇
import os
import platform
sysos = platform.platform()
import random
randnum = random.randint(0,2)
rps = [rock,paper,scissors]
while True:
  userselect = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
  if userselect >=0 and userselect < 3:
    break
  else:
    if sysos[0] == "Windows":
      os.system('cls')
    else:
      os.system('clear')
    print("Please select a number between 0 and 2")

print(f"{rps[userselect]}\n")
if userselect == randnum:
  print(f"Computer chooses:\n{rps[randnum]}\nIt's a tie!")
elif userselect == randnum - 1:
  print(f"Computer chooses:\n{rps[randnum]}\nYou lose!")
elif userselect == randnum + 1:
  print(f"Computer chooses:\n{rps[randnum]}\nYou Win!")
elif userselect == randnum - 2:
  print(f"Computer chooses:\n{rps[randnum]}\nYou Win!")
elif userselect == randnum + 2:
  print(f"Computer chooses:\n{rps[randnum]}\nYou lose!")