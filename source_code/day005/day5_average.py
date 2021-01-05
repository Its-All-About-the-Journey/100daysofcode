student_heights = input("Input a list of student heights: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

students = 0 # < --- initied the list with 0
for student in student_heights:
    students += student  # < --- Add each height each other to the students list for a total heights
    #print(students)  # < --- Verified the output

average = 0
for student in student_heights:
    average += 1  # < --- Calculate for the average (if you have 5 input, the loop will run 5 times, and average will be 5)
    #print(average) # < --- Verified the output

total_average = students / average  # < --- Calculate the average by dividing the total student's height per the number of students
print(f"The average of student's height is: {round(total_average)}")

