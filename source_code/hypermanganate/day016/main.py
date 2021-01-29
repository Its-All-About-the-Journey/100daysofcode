#!/usr/bin/env python3
# 100 Days of Code : Day 16 Project
# Coffee Machine OOP
# Adam Pawlowski (@hypermanganate)

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Func


def prompt_for_action(menu):
    """
    Prompt the user to choose a machine action.

    Returns the choice.
    """

    choice = None

    while choice not in ['off', 'report'] + menu.get_items().split('/'):
        choice = input("What would you like? (espresso/latte/cappuccino): ")

    return choice


def do_coffee_loop():
    """
    Repeat endlessly asking the user to make a choice,
    until the loop is broken by turning the machine off.
    """

    coffee_maker = CoffeeMaker()
    drinks_menu = Menu()
    money_machine = MoneyMachine()

    while True:
        action = prompt_for_action(drinks_menu)
        if action == "off":
            break
        elif action == "report":
            print("Machine Report:")
            coffee_maker.report()
            money_machine.report()
        else:
            # A cup of coffee has been requested
            drink = drinks_menu.find_drink(action)
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)

    return

# Main


if __name__ == '__main__':
    do_coffee_loop()
