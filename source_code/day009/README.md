# DAY 9

Silent Auction

# Description

A program which allows you to conduct a "silent auction" using a computer terminal.

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
## Student Scores

```
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

student_grades = {}

for student in student_scores:
  if student_scores[student] > 90:
    student_grades[student] = "Outstanding"
  elif student_scores[student] > 80:
    student_grades[student] = "Exceeds Expectations"
  elif student_scores[student] > 70:
    student_grades[student] = "Acceptable"  
  else:
    student_grades[student] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)
```

## Travel Log Adder
```

def add_new_country(country, times_visited, cities):
   travel_log.append(
     {
       "country": country,
       "visits": times_visited,
       "cities": cities
     }
   )

```

