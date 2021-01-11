# Q1
# Print Apples
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
print(fruits[2])
print(fruits[-5])

# Q2
# Replaces last item on the list with Melons and adds Lemons to the end of the list
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
fruits[-1] = "Melons"
fruits.append("Lemons")
print(fruits)

# Q3
# First input selects list, second input select specific item
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen[1][1])

# 3rd input prints specific letter/index of the item
print(dirty_dozen[1][1][0])