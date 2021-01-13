from random import randint

print("""

  ██████  ██▓ ███▄    █  ██▓  ██████ ▄▄▄█████▓▓█████  ██▀███  
▒██    ▒ ▓██▒ ██ ▀█   █ ▓██▒▒██    ▒ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒
░ ▓██▄   ▒██▒▓██  ▀█ ██▒▒██▒░ ▓██▄   ▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒
  ▒   ██▒░██░▓██▒  ▐▌██▒░██░  ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄  
▒██████▒▒░██░▒██░   ▓██░░██░▒██████▒▒  ▒██▒ ░ ░▒████▒░██▓ ▒██▒
▒ ▒▓▒ ▒ ░░▓  ░ ▒░   ▒ ▒ ░▓  ▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░▒  ░ ░ ▒ ░░ ░░   ░ ▒░ ▒ ░░ ░▒  ░ ░    ░     ░ ░  ░  ░▒ ░ ▒░
░  ░  ░   ▒ ░   ░   ░ ░  ▒ ░░  ░  ░    ░         ░     ░░   ░ 
 ███▄ ░  █░ █    ██  ███▄░▄███▓ ▄▄▄▄   ▓█████  ██▀███   ░██████ 
 ██ ▀█   █  ██  ▓██▒▓██▒▀█▀ ██▒▓█████▄ ▓█   ▀ ▓██ ▒ ██▒▒██    ▒ 
▓██  ▀█ ██▒▓██  ▒██░▓██    ▓██░▒██▒ ▄██▒███   ▓██ ░▄█ ▒░ ▓██▄   
▓██▒  ▐▌██▒▓▓█  ░██░▒██    ▒██ ▒██░█▀  ▒▓█  ▄ ▒██▀▀█▄    ▒   ██▒
▒██░   ▓██░▒▒█████▓ ▒██▒   ░██▒░▓█  ▀█▓░▒████▒░██▓ ▒██▒▒██████▒▒
░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ░ ▒░   ░  ░░▒▓███▀▒░░ ▒░ ░░ ▒▓ ░▒▓░▒ ▒▓▒ ▒ ░
░ ░░   ░ ▒░░░▒░ ░ ░ ░  ░      ░▒░▒   ░  ░ ░  ░  ░▒ ░ ▒░░ ░▒  ░ ░
   ░   ░ ░  ░░░ ░ ░ ░      ░    ░    ░    ░     ░░   ░ ░  ░  ░  
         ░    ░            ░    ░         ░  ░   ░           ░  
                                     ░                          
""")

goal = randint(lower := 1, upper := 100)
print(f"i am thinking of a number between {lower} and {upper}.\n")

attempts = 10 if input("would you like it hard or easy? ") == "easy" else 5
print(f"\nyou will have {attempts} attempts...let's go...\n")

attempt = 0
while (attempt := attempt + 1) <= attempts:
    guess = int(input(f"guess #{attempt}: "))
    if guessed := guess == goal:
        break
    print(f"{guess} is too {'low' if guess < goal else 'high'}\n")
    
print(f"{'you failed' if not guessed else 'you win'}! it was {goal}!")