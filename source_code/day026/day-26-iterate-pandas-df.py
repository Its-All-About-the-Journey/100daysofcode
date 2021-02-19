student_dict = {
    "student" : ["Angela", "James", "Lily"],
    "score" : [56, 76, 98]
}

#Looping through dictionaries
#for (key, value) in student_dict.items():
#    print(key)
#    print(value)
    

import pandas
student_data_frame = pandas.DataFrame(student_dict)
#print(student_data_frame)

#for (key,value) in student_data_frame.items():
#    print(key)
#    print(value)

#Loop through rows of dataframe rather than columns
for (index, row) in student_data_frame.iterrows():
    #print(row)
    #print(row.student) #Print student names
    #print(row.score) #Print score for student
    if row.student == "Angela":
        print(row.score)