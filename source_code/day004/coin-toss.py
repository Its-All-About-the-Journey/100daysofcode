import random

print("Let's flip a coin!")

coin_toss = random.randint(0,1)

if coin_toss == 0:
  print("Tails")
else:
  print("Heads")