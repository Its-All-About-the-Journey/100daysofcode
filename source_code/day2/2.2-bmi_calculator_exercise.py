# 🚨 Don't change the code below 👇
height = input("\nEnter your height in m: ")
weight = input("\nEnter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
ht = float(height)
wt = float(weight)
ht_1 = ht*ht
result = int(wt / ht_1)

print(result)

# Solution from course

bmi = float(weight) / float(height) ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)