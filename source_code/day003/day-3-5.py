print("Welcome to the Love Calculator!")
name = input("What is your name?\n").lower()
name += input("What is their name?\n").lower()
count_love = 0
count_true = 0
count_true += name.count("e")
count_love = count_true
count_true += name.count("t")
count_true += name.count("r")
count_true += name.count("u")
count_love += name.count("l")
count_love += name.count("o")
count_love += name.count("v")

love_score = int(str(count_true) + str(count_love))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 and love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")