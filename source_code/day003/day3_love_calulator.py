
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

two_name = name1 + name2
lower_case_name = two_name.lower()

t = lower_case_name.count('t')
r = lower_case_name.count('r')
u = lower_case_name.count('u')
e = lower_case_name.count('e')

l = lower_case_name.count('l')
o = lower_case_name.count('o')
v = lower_case_name.count('v')
e = lower_case_name.count('e')

true = t + r + u + e
love = l + o + v + e

contability = str(true) + str(love)

if contability < str(10) or contability > str(90):
    print(f"Your score is {contability}, you go together like coke and mentos.")
elif contability >= str(40) and contability <= str(50):
    print(f"Your score is {contability}, you are alright together.")
else:
    print(f"Your score is {contability}")