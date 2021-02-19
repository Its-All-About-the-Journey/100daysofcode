with open("source_code/day026/file1.txt", "r") as file1:
    list1 = file1.readlines()

with open("source_code/day026/file2.txt", "r") as file2:
    list2 = file2.readlines()

result = [int(number) for number in list1 if number in list2]

# Write your code above 👆

print(result)

