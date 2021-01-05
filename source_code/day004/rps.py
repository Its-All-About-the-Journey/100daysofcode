# final - Rock Paper Scissors
# ---------------------------------------
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

from random import randint
choices = [rock, paper, scissors]
rock, paper, scissors = range(3)

# Player 1
player1 = int(input("0 = Rock; 1 = Paper; 2 = Scissors: "))
print(choices[player1])

# CPU1
cpu1 = randint(0, 2)
print(choices[cpu1])

if player1 == cpu1:
  print("Draw!")
elif ((player1 == rock and cpu1 == scissors)
  or (player1 == paper and cpu1 == rock)
  or (player1 == scissors and cpu1 == paper)):
  print("You Win!")
else:
  print("You Lose!")