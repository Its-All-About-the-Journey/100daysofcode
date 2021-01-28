student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.

student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇

# student_grades["Harry"] = "Exceeds Expectation"
# student_grades["Ron"] = "Acceptable"
# student_grades["Hermione"] = "Outstanding"
# student_grades["Draco"] = "Acceptable"
# student_grades["Neville"] = "Fail"

# student_grades = {
#     "Harry": "Exceeds Expectation",
#     "Ron": "Acceptable",
#     "Hermione": "Outstanding",
#     "Draco": "Acceptable",
#     "Neville": "Fail"
# }

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Oustanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)





