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

OPTIONS_MAIN = [
    "espresso",
    "latte",
    "cappuccino",
]

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

bank = 0

# TODO: refactor this to pull from MENU instead of a separate list


OPTIONS_SECONDARY = [
    "off",
    "report",
]


def drink_selection():
    proper_selection = False
    drink_choice = ""
    while not proper_selection:
        drink_choice = str.lower(input("What would you like? (espresso/latte/cappuccino): "))
        if drink_choice in OPTIONS_MAIN or drink_choice in OPTIONS_SECONDARY:
            proper_selection = True
        else:
            print("Please select from the available options. \n ")
    return drink_choice


def turn_off(drink):
    if drink == "off":
        return True


def print_report():
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: ${bank}")
    print("")


def check_resources(drink):
    score = 0
    for a_option, b_option in MENU[drink]['ingredients'].items():
        if b_option > resources[a_option]:
            print(f"Sorry, there is not enough {a_option}")
            score -= 10
        else:
            score += 1
    if score < 0:
        return False
    else:
        return True


def process_coins():
    print("Please insert coins.")
    pennies = int(input("How many pennies? ")) * 1
    nickels = int(input("How many nickels? ")) * 5
    dimes = int(input("How many dimes? ")) * 10
    quarters = int(input("How many quarters? ")) * 25

    # Create a dollar amount based on the total coins collected
    coinage = pennies + nickels + dimes + quarters
    dollar_amount = round((coinage/100), 2)
    return dollar_amount


def valid_money(trans, drink):
    sufficient = False
    drink_cost = MENU[drink]["cost"]
    if trans >= drink_cost:
        leftover_change = round(trans - drink_cost, 2)
        print(f"Your change is ${leftover_change}.")
        sufficient = True
        return leftover_change, sufficient
    else:
        return sufficient


brewing_coffee = True
while brewing_coffee:
    # initial step of asking for a selection
    brew = drink_selection()

    # turns off machine and ends script
    if turn_off(brew):
        print("Turning off...")
        brewing_coffee = False

    # prints a report
    if brew == "report":
        print_report()

    # if not a report or "off", then go through rest of the logic
    if brew in OPTIONS_MAIN:
        available = check_resources(brew)
        if available:
            transaction = process_coins()
            sufficientFunds = valid_money(transaction, brew)
            change = sufficientFunds[0]
            if sufficientFunds[1]:
                bank += MENU[brew]['cost']
                # print(bank)
                for x, y in MENU[brew]['ingredients'].items():
                    resources[x] -= y
                print("Here is your latte ☕️. Enjoy!")
            else:
                print("Sorry, that's not enough money. Money refunded.")
        else:
            brewing_coffee = False
