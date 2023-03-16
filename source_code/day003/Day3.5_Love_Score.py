# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


namelow = name1.lower() + name2.lower()
truecount = 0
truecount += namelow.count("t")
truecount += namelow.count("r")
truecount += namelow.count("u")
truecount += namelow.count("e")
lovecount = 0
lovecount += namelow.count("l")
lovecount += namelow.count("o")
lovecount += namelow.count("v")
lovecount += namelow.count("e")

lovescore = int(str(truecount) + str(lovecount))

if lovescore < 10 or lovescore > 90:
    print(f"Your score is {lovescore}, you go together like coke and mentos.")
elif lovescore >= 40 and lovescore <= 50:
    print(f"Your score is {lovescore}, you are alright together.")
else:
    print(f"Your score is {lovescore}.")
