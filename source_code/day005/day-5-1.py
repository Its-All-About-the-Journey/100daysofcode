# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total_height = 0
students = 0
for height in student_heights:
  total_height += height
  students += 1

average_height = round(total_height / students)
print(f"Average height of all students is {average_height}")


