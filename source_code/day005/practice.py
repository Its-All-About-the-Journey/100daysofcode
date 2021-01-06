# 5.1 - average heights
# --------------------------------------
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

i = total_height = 0
for student_height in student_heights:
i += 1
total_height += student_height
average_height = round(total_height / i)

print(f"Average student height is {average_height}")

