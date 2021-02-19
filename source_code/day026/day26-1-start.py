# List Comprehension, increment list by 1
#test = [1,2,3,4,5]
#new_list = [i + 1 for i in test]
#print(new_list)

#range_list = [i * 2 for i in range(1,5)]
#print(range_list)
#multiply_evens = [i * 2 for i in range(1,5) if i % 2 == 0]
#print(multiply_evens)

#name = "jacob"
#new_list = [letter for letter in name]
#print(new_list)

#Only print names 4 letters or less
#names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

#names_list = [name for name in names if len(name) <= 4]
#print(names_list)

#Uppercase names longer than 5 letters
#upper_names = [name.upper() for name in names if len(name) > 5]
#print(upper_names)

#Dictionary comprehension
import random
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

#student_score = {
#    "Alex": 89
#    "Beth": 98
#}

student_scores = {name:random.randint(1,100) for name in names}
print(student_scores)

#Dictionary comprehension to create new dictionary
past_students = {student:score for (student,score) in student_scores.items() if score >= 60}
print(past_students)

