# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lowercase_names = f'{name1}{name2}'.lower()

sum = 0
for character in 'true':
    sum += lowercase_names.count(character)

sum *= 10

for character in 'love':
    sum += lowercase_names.count(character)

# Cases
#     10 > sum or sum >= 90
#     50 > sum > 40
#     all others: score


if sum < 10 or sum >= 90:
    print(f'Your score is {sum}, you go together like coke and mentos.')

elif sum < 50 and sum > 40:
    print(f'Your score is {sum}, you are alright together.')

else:
    print(f'Your score is {sum}.')

