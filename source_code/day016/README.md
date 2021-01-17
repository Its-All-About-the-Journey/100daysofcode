# DAY 16

Object Oriented Coffee Pot

# Description

An object oriented version of the Coffee Pot.

# Environment
OS: Ubuntu Bionic

Python version: 3.8.7

# Dependencies

Coffee Maker
Menu
Money Machine

# How to run script
```
Call the script.

Follow the prompts to order 'coffee'. Note, you cannot actually order coffee.

Type 'report' to see a status of available resources.

Type 'off' to turn the machine off.

```

# Sample output
```
What would you like? (espresso/latte/cappuccino): latte
Please insert coins.
How many quarters?: 99
How many dimes?: 0
How many nickles?: 0
How many pennies?: 0
Here is $22.25 in change.
Here is your latte ☕️. Enjoy!
What would you like? (espresso/latte/cappuccino): cappuccino
Sorry there is not enough water.
What would you like? (espresso/latte/cappuccino): report
Machine Report:
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
What would you like? (espresso/latte/cappuccino): iff
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
