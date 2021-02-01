
# DAY 26

Phoenetic Alphabet Tool

# Description

# Environment
OS: Ubuntu Bionic

Python version: 3.8.7

# Dependencies

# How to run script
```
enter instructions here
```

# Sample output

```
NATO Wordulator

What word do you need to decode? fart
Your NATO word is: Foxtrot Alfa Romeo Tango
```

# Other Exercises

## Double Output
```
doubled_numbers = [number * 2 for number in range(1, 5)]
print(doubled_numbers)
```

## Short Names
```
names = ["Alex", "Beth", "Caroline", "Dave", " Eleanor", "Freddie"]
short_names = [name for name in names if len(name) <= 4]
print(short_names)
```

## Upper Longer Names
```
names = ["Alex", "Beth", "Caroline", "Dave", " Eleanor", "Freddie"]
longer_upper_names = [name.upper() for name in names if len(name) >= 5]
print(longer_upper_names)
```

## Squared Numbers
```
squared_numbers = [number**2 for number in numbers]
```

## Even Numbers
```
result = [number for number in numbers if not number % 2]
```

## Numbers in both files
```
This didn't work:

with open("./file1.txt") as file1:
  with open("./file2.txt") as file2:
    result = [int(number) for number in file2.readlines() if number in file1.readlines()]

This did:

file1 = open("./file1.txt", "r").readlines()
file2 = open("./file2.txt", "r").readlines()

result = [int(number) for number in file1 if number in file2]
```

## 50 States Game Update

I did not create a new list since the game requirements weren't that I don't manipulate the original data object.
So, there was nothing for me to do here.

As a consequence, I also can't easily come up with a list of "guessed" states.

## Letter counts for a sentence

```
result = {word:len(word) for word in sentence.split(" ")}
```

## C to F converter

```
def temp_f(temp_c: int):
  return (temp_c * 9/5) + 32

weather_f = {day:temp_f(temp) for (day, temp) in weather_c.items()}
```


