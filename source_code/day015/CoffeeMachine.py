import os
import platform
import time

_sysos_ = platform.system()
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
    "money": 0,
}

coins = {"quarters": .25,
         "dimes": .10,
         "nickles": .05,
         "pennies": .01}

commands = ["espresso", "latte", "cappuccino", "off", "prices", "report", "refill"]


# TODO: 2. Check if resources are sufficient to make the drink and if not respond with: "Sorry there is not enough __"
def check_inventory(_order_):
    """Pass the name of the drink being ordered to tell customer if their drink can or can't be made."""
    missing = 0
    for item in MENU[_order_]["ingredients"]:
        if resources[item] < MENU[_order_]["ingredients"][item]:
            print(f"Sorry there is not enough {item}.")
            missing += 1
    if missing > 0:
        return False
    else:
        print("Please insert coins.")
        return True


# TODO: 3. Request payment in coins, list the coins from largest to smallest, add up the coins.
# TODO: 4. Check if transaction successful, if enough money then return change, if not return all money and reply
#  "Sorry that's not enough money. Money refunded." | "Here is $__change__ in change."

def collect_money(_order_):
    """Submit drink name, collects payment from user and returns amount paid."""
    price = MENU[_order_]["cost"]
    payment = 0
    for coin in coins:
        if payment < price:
            print(f"Amount required: ${round(price - payment, 2)}")
            payment += int(input(f" How many {coin}?: ")) * coins[coin]
            print(f"Amount entered: {round(payment, 2)}")
    return payment


def ring_up(_order_):
    """Submit name of drink being ordered, returns value of payment."""
    payment = collect_money(_order_)
    # round(payment, 2)
    if payment < MENU[_order_]["cost"]:
        print(f"Sorry that's not enough money. ${payment} refunded.")
        return 0
    elif payment > MENU[_order_]["cost"]:
        change = round(payment - MENU[_order_]["cost"], 2)
        deduct_inventory(_order_)
        print(f"Here is ${change} in change.")
        print(f"Here is your {_order_}. Enjoy! ☕ ")
        return MENU[_order_]["cost"]
    else:
        deduct_inventory(_order_)
        print(f"Here is your {_order_}. Enjoy! ☕ ")
        return MENU[_order_]["cost"]


# TODO: 5. Make the coffee, deduct the resourced needed to make the drink from the total resources and add the money.
#  “Here is your __drink__. Enjoy!”

def deduct_inventory(_order_):
    for item in MENU[_order_]["ingredients"]:
        resources[item] -= MENU[_order_]["ingredients"][item]


# TODO: 6. Print report of all coffee resources if user types "report"
def report():
    for each in resources:
        if each == "water" or each == "milk":
            print(f"{each.title()}: {resources[each]}ml")
        elif each == "coffee":
            print(f"{each.title()}: {resources[each]}g")
        else:
            print(f"{each.title()}: ${resources[each]}")


def prices():
    for drink in MENU:
        print(f"The {drink} costs: ${MENU[drink]['cost']}")


def refill():
    """Asks user for item to be refilled and refills that item to max."""
    item = input("What would you like to refill? ('Water', 'Milk', 'Coffee'): ").lower()
    while True:
        if item == "water":
            resources["water"] = 300
            break
        elif item == "milk":
            resources["milk"] = 200
            break
        elif item == "coffee":
            resources["coffee"] = 100
            break
        else:
            print("Bad value, try again.")
            time.sleep(1)
            print("                    ", end='\r')
            print("\x1b[1A", end='\r')


def blank_line(length):
    """Use to erase the previous 1 line.  Provide the length of the line."""
    print("\x1b[1A" + " "*length, end='\r')


if _sysos_ == "Windows":
    os.system('cls')
else:
    os.system('clear')

running = True
while running:
    # TODO: 1. Prompt user with "What would you like? (espresso/latte/cappuccino):"
    print("Welcome to the coffee vending machine.")
    print(f"Commands: {commands}")
    while True:
        command = input(" What would you like? (espresso/latte/cappuccino): ")
        if command in commands:
            break
        else:
            blank_line(len(command) + 51)
    if command == "report":
        report()
        input("Press [Enter] to continue.")
    elif command == "off":
        # TODO: 7. exit the program if user types "off"
        print("Powering down.")
        exit()
    elif command == "prices":
        prices()
        input("Press [Enter] to continue.")
    elif command == "refill":
        refill()
    else:
        if check_inventory(command):
            resources["money"] += ring_up(command)
            input("Press [Enter] to continue.")
        else:
            input("Press [Enter] to continue.")
    if _sysos_ == "Windows":
        os.system('cls')
    else:
        os.system('clear')
