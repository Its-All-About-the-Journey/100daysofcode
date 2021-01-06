# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

num_students = height_sum = 0

for student_height in student_heights:
    num_students += 1
    height_sum += student_height

avg_height = round(height_sum / num_students)

print(avg_height)