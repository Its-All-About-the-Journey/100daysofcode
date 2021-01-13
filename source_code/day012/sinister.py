logo = """

  ██████  ██▓ ███▄    █  ██▓  ██████ ▄▄▄█████▓▓█████  ██▀███  
▒██    ▒ ▓██▒ ██ ▀█   █ ▓██▒▒██    ▒ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒
░ ▓██▄   ▒██▒▓██  ▀█ ██▒▒██▒░ ▓██▄   ▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒
  ▒   ██▒░██░▓██▒  ▐▌██▒░██░  ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄  
▒██████▒▒░██░▒██░   ▓██░░██░▒██████▒▒  ▒██▒ ░ ░▒████▒░██▓ ▒██▒
▒ ▒▓▒ ▒ ░░▓  ░ ▒░   ▒ ▒ ░▓  ▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░▒  ░ ░ ▒ ░░ ░░   ░ ▒░ ▒ ░░ ░▒  ░ ░    ░     ░ ░  ░  ░▒ ░ ▒░
░  ░  ░   ▒ ░   ░   ░ ░  ▒ ░░  ░  ░    ░         ░     ░░   ░ 
      ░   ░           ░  ░        ░              ░  ░   ░     
                                                              

"""

print(logo)

from random import randint
target = randint(1, 100)

print("sinister is thinking of a number between 1 and 100.\n")
difficulty = input("hard or easy: ")
attempts = 10 if difficulty == "easy" else 5
print(f"\nyou will have {attempts} attemps...let's go...\n")
attempt = 1

guessed = False
while attempts > attempt:
    attempt += 1
    guess = int(input("guess: "))
    if guess == target:
        guessed = True
        break
    elif guess < target:
        print(f"{guess} is too low")
    else:
        print(f"{guess} is too high")

if guessed:
    print("you guessed it!")
else:
    print(f"you failed it! it was {target}!")