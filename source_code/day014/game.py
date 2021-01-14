from random import shuffle
from gamedata import data
from replit import clear

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

# shuffle the data set
shuffle(data)

score = 0
for i in range(1, len(data)):

    # print logo
    clear()
    print(logo)
    print()
    
    # if score == 0, then this is round 1
    if score == 0:

        # on round 1, we need two randos
        instas = [data[i-1], data[i]]

    # otherwise, they've at least gotten 1 answer right so far
    else:

        # on all subsequent rounds...
        # keep the user updated on their score
        print(f"You're right! Current score: {score}.")
        print()
        
        # move slot B into slot A
        instas[0] = instas[1]

        # pull new B from data set
        instas[1] = data[i]

    # let them know who A is
    print(f"Compare A: {instas[0]['name']}, a {instas[0]['description']}, from {instas[0]['country']}.")

    # print fancy VS mini logo
    print(vs)

    # let them know who B is
    print(f"Against B: {instas[1]['name']}, a {instas[1]['description']}, from {instas[1]['country']}.")

    # determine for ourselves who the winner is
    winner = "A" if instas[0]['follower_count'] > instas[1]['follower_count'] else "B"

    # give the dev a break
    # print()
    # print(f"Pssst, the winner is {winner}!")

    # ask the user who they think the winner is
    print()
    guess = input("Who has more followers? Type 'A' or 'B': ")

    # if they were wrong, just quit
    if guess != winner: break

    # else, increment the score and keep it going...
    score += 1

clear()
print(logo)
print()
print(f"Final score: {score}!")
print()
if score == len(data) - 1:
    print("You got every single one right!")
else:
    print("Sorry, that's wrong")