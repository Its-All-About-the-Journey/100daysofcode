# DAY 5

Password Generator

# Description

# Environment
OS: Ubuntu Bionic

Python version: 3.6.9

# Dependencies

None

# How to run script
```
```

# Sample output
```
```

# Other Exercises

Average Height

```
total_height = 0
number_of_students = 0

for student_height in student_heights:
  total_height += student_height
  number_of_students += 1

print(round(total_height / number_of_students))
```

High Score

```
high_score = 0 

for score in student_scores:
    if score > high_score: high_score = score 

print(f"""The highest score in the class is: {high_score}""")
```

Even Number Adder

```
total = 0
for number in range(1,101):
  if not number % 2: total += number

print(total)
```

FizzBuzz

```
for number in range(1, 101):
  out = ''
  if not number % 3:
    out += 'Fizz'
  if not number % 5:
    out += 'Buzz'
  if out == '':
    out = number
  print(out)
```

