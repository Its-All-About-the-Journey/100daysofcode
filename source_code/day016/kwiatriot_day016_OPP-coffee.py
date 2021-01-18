"""
Day 016 of the 100 Days of Code course
Author: Wayne Kwiat
Date: 1/16/2021

"""

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_transaction = MoneyMachine()
drink_dispenser = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        drink_dispenser.report()
        money_transaction.report()
    else:
        drink = menu.find_drink(choice)
        ingredient_check = drink_dispenser.is_resource_sufficient(drink)
        payment = money_transaction.make_payment(drink.cost)
        if ingredient_check and payment:
            drink_dispenser.make_coffee(drink)

