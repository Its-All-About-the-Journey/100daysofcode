
# DAY 3
Tresure Island Game

# Description

You begin the adventure of day three at Treasure Island. 
You seek enrichment, but many perils lie before you!
Take part in this text adventure game to see if you will survive!

# Environment
OS: Ubuntu Bionic

Python version: 3.6.9

# Dependencies

# How to run script
```
Simply call the script.
Follow the story, and make your choices when prompted.
Choose wisely, and type carefully!
```

# Sample output
```
*SPOILERS*
```
# Other Exercises

"Even/Odd Detector"

```
print("Even") if number % 2 == 0 else print("Odd")
```

"BMIalyzer"

```
bmi = round(weight / height ** 2)

if bmi < 18.5:
  diagnosis = "are underweight"
elif bmi < 25:
  diagnosis = "have a normal weight"
elif bmi < 30:
  diagnosis = "are slightly overweight"
elif bmi < 35: 
  diagnosis = "are obese"
else:
  diagnosis = "are clinically obese"

print(f"""Your BMI is {bmi}, you {diagnosis}.""")
```

"Leap Year Checker"

```
if not year % 4 and (year % 100 or (not year % 100 and not year % 400)):
  print ("Leap year.")
else:
  print ("Not leap year.")
```

"Pizza Ordering"

```
if size == "S":
  bill = 15
elif size == "M":
  bill = 20
else: 
  bill = 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3

if extra_cheese == "Y":
  bill += 1

print(f""Your final bill is: ${bill}.""")
```

"Love-O-Meter"

```
true_score, love_score = 0,0

for letter in "true":
  true_score += str(name1+name2.lower()).count(letter)

for letter in "love":
  love_score += str(name1+name2.lower()).count(letter)

true_love_score = int(f"{true_score}{love_score}")  

message = ''

if true_love_score < 10 or true_love_score > 90:
  message = ", you go together like coke and mentos"
if true_love_score > 40 and true_love_score < 50:
  message = ", you are alright together"

print(f"""Your score is {true_love_score}{message}.""")
```

