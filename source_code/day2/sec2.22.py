# Division becomes a float
print(8 / 3)

# Division wit int cuts off decimal
print(int(8 / 3))

# Rounds up or down
print(round(8 / 3))

# 3rd number identifies how many decimal points, separated by a comma ,
print(round(8 / 3, 2))

# Floor Division - This identifies how many times the primary number can be divided into
print(8 // 3)

# Integer Data Type
print(type(8 // 3))

# Float Data Type
print(type(8 / 3))

# Save results into a variable
result = 4 / 2
result /= 2
print(result)

# 2nd Example for variable
score = 0
score += 1
print(score)

score = 0
score -= 1
print(score)

score = 0
score /= 1
print(score)

score = 0
score *= 1
print(score)

# f-string goes in front of quotes
score = 0
height = 1.8
isWinning = True

print(f"your score is {score}, your height is {height}m. You are winning is {isWinning}.")