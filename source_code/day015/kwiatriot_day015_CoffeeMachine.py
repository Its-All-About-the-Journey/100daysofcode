"""
Day 015 of the 100 Days of Code course
Author: Wayne Kwiat
Date: 1/15/2021

"""
import sys


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

coins = {
    "penny": .01,
    "nickel": .05,
    "dime": .10,
    "quarter": .25
}


def check_payment(penny, nickel, dime, quarter):
    """This function takes in the coins added by the user and returns the total amount entered"""
    total_penny = penny * coins["penny"]
    total_nickel = nickel * coins["nickel"]
    total_dime = dime * coins["dime"]
    total_quarter = quarter * coins["quarter"]
    total_amount = total_penny + total_nickel + total_dime + total_quarter
    return total_amount


def dispense_drink(order, order_ingredients):
    """Remove ingredients from resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {order}. Enjoy!")


def process_transaction():
    """Returns total calculated from coins deposited"""
    print("Please insert coins.\n")
    inserted_penny = int(input("how many pennies?: "))
    inserted_nickel = int(input("how many nickels?: "))
    inserted_dime = int(input("how many dimes?: "))
    inserted_quarter = int(input("how many quarters?: "))
    payment = check_payment(inserted_penny, inserted_nickel, inserted_dime, inserted_quarter)
    return payment


def prompt():
    """This function displays the prompt to the user"""
    return input("What would you like? (espresso/latte/cappuccino): ")


def report():
    """This function prints the status of the machines resources"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def resource_check(selection):
    """This function takes in the selection and checks if the machine can make it"""
    for item in selection:
        if selection[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def transaction(money_deposited, drink_cost):
    """"Function returns True is payment is accepted or False is not enough money was entered"""
    if money_deposited >= drink_cost:
        change = round(money_deposited - drink_cost, 2)
        print(f"Your change is ${change}.")
        resources["money"] += drink_cost
        return True
    else:
        print("You did not deposit enough money. Money refunded.")
        return False


machine_on = True

while machine_on:
    user_selection = input("What would you like? espresso/latte/cappuccino: ")
    if user_selection == "off":
        machine_on = False
        sys.exit(0)
    elif user_selection == "report":
        report()
    else:
        drink = MENU[user_selection]
        if resource_check(drink["ingredients"]):
            payment = process_transaction()
            if transaction(payment, drink["cost"]):
                dispense_drink(user_selection, drink["ingredients"])
