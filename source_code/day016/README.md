# DAY 16

Object Oriented Coffee Pot

# Description

An object oriented version of the Coffee Pot.

# Environment
OS: Ubuntu Bionic

Python version: 3.6.9

# Dependencies

Machine Data Dictionary

# How to run script
```
Call the script.

Follow the prompts to order 'coffee'. Note, you cannot actually order coffee.

Type 'report' to see a status of available resources.

Type 'off' to turn the machine off.

```

# Sample output
```
What would you like? (espresso/latte/cappuccino): espresso
Espresso costs $1.50
Give me your money
How many pennies?: 0
How many nickels?: 0
How many dimes?: 0
How many quarters?: 999999999
Here is $249999998.25 in change.
Here is your espresso ☕. Enjoy!
What would you like? (espresso/latte/cappuccino): report
Coffee Machine Supply Status:
* Water: 250ml
* Milk: 200ml
* Coffee: 82g
* Money: $1.50
What would you like? (espresso/latte/cappuccino): off
```

## Other Exercises
# Logo/Turtle

```
from turtle import Screen, Turtle

my_screen = Screen()
logo = Turtle()

logo.shape("turtle")
logo.color("chartreuse2")
logo.forward(50)

my_screen.exitonclick()
```

# PrettyTable Package

```
from prettytable import PrettyTable

table = PrettyTable()
# .add_column(colname, [col,data])

table.add_column('Bland Spice', ['Oregano', 'Parsley', 'Taco',
                 'Pizza', 'Italian', 'Montrael'])

table.add_column('Bland Receipe', ['Chicken', 'Potato', 'Beef',
                 'DiGiorno', 'Also Chicken', 'Grilled Whatever'])

table.align = 'l'

print(table)
```
