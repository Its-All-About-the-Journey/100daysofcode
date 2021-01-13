#Write your code below this row 👇
total = 0
for number in range(2, 101, 2):
    total += number
print(total)

total2 = 0
for number in range(2, 101, 2):
    if number % 2 == 0:
        total2 += number
print(total2)
