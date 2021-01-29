
# DAY 4

# Description

Rock Paper Scissors

# Environment
OS: Ubuntu Bionic

Python version: 3.6.9

# Dependencies

None, core.

# How to run script
```
Simply call the script.
You'll be prompted to choose Rock, Paper, or Scissors to compete against the computer.

See how many times you can win, and then try and beat that record!

```

# Sample output
```
Rock Paper Scissors
What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors (Enter to quit): 1
You choose paper:

    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

Computer chooses scissors:

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

You chose paper, and computer chose scissors.

Paper loses to scissors. Sorry, you lose.

  ****************************
  * | Player  | | Computer | *
  * ----------- ------------ *
  *      0            1      *
  ****************************

Play again? (y/n) y
	
```

# Other Exercises

Coin Toss Program
```
print("Heads") if random.randint(0,1) else print("Tails")

```

London Banker's Lunch Decider
```
import random

print(f"""{names[random.randint(0,(len(names) - 1))]} is going to buy the meal today!""")
```

Treasure Map
```
map[int(position[1]) - 1][int(position[0]) - 1] = "X"
```
