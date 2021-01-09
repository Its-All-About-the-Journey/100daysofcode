programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",

    "Function": "A piece of code that you can easily call over and over again."
}

# 9.1 - grading
# -----------------------------------------------------------
def one():
    student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99, 
    "Draco": 74,
    "Neville": 62,
    }
    # 🚨 Don't change the code above 👆

    #TODO-1: Create an empty dictionary called student_grades.
    student_grades = {}

    #TODO-2: Write your code below to add the grades to student_grades.👇
    for student in student_scores:
        score = student_scores[student]
        if score <= 70:
            grade = "Fail"
        elif score <= 80:
            grade = "Acceptable"
        elif score <= 90:
            grade = "Exceeds Expectations"
        else:
            grade = "Outstanding"
        student_grades[student] = grade
        

    # 🚨 Don't change the code below 👇
    print(student_grades)

# 9.2 - travel log
# -----------------------------------------------------------
def two():
    travel_log = [
    {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
    },
    {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
    ]
    #🚨 Do NOT change the code above

    #TODO: Write the function that will allow new countries
    #to be added to the travel_log. 👇

    def add_new_country(country, visits, cities):
        travel_log.append({
            "country": country,
            "visits": visits,
            "cities": cities
        })


    #🚨 Do not change the code below
    add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
    print(travel_log)