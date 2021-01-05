student_scores = input("Input a list of student heights: ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

maximum = 0
for numbers in student_scores:
    if numbers > maximum:
        maximum = numbers
        
print(f"The highest score in the class is: {maximum}")