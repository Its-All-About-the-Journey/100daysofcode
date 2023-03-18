# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

list_len = 0
avg_height = 0
for m in student_heights:
    list_len += 1
for h in student_heights:
    avg_height += h
avg_height = round(avg_height / list_len)

print(avg_height)