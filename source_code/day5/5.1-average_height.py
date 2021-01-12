# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Can't use the following functions
# print(len(student_heights))
# print(sum(student_heights))

# Use a for loop to add all the numbers
# Use a for loop to calculate the amount of items in the list

# Example Input
# 180 124 165 173 189 169 146

#Write your code below this row 👇
# print("The list is: " + str(student_heights))

total_height = 0
num_of_students = 0
for x in student_heights:
    total_height += x
    num_of_students += 1
    average = total_height / num_of_students
    roundup = round(average)
print("The the number of students is: " + str(num_of_students))
print("The total height for the students are: " + str(total_height))
print("The average height is: " + str(average))
print("The average height rounded up is: " + str(roundup))

# Solution from Exercise
total_height = 0
for height in student_heights:
    total_height += height
print(total_height)

num_of_students = 0
for students in student_heights:
    num_of_students += 1
print(num_of_students)

average_height = round(total_height / num_of_students)
print(average_height)


