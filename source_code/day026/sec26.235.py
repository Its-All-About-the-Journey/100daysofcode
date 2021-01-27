with open("file1.txt") as file1_in:
    file1 = file1_in.read().splitlines()

with open("file2.txt") as files2_in:
    file2 = files2_in.read().splitlines()

result = [int(line) for line in file1 if line in file2]
# Write your code above 👆

print(result)


