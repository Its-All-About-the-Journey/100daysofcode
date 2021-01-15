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
    "water": {"amount": 300, "unit": "ml"},
    "milk": {"amount": 200, "unit": "ml"},
    "coffee": {"amount": 100, "unit": "g"},
    "money": {"amount": 0, "unit": "$"}
}

def report():
    """Prints an inventory report"""
    for item, details in resources.items():
        if item == "money":
            quantity = f"{details['unit']}{details['amount']:.2f}"
        else:
            quantity = f"{details['amount']}{details['unit']}"
        print(f"{item.title()}: {quantity}")
        
def ingredients(choice):
    """Returns the needed ingredients to make a certain drink choice"""
    return MENU[choice]["ingredients"]

def enough(ingredients):
    """Checks a list of required ingredients to see if we have enough"""
    lacking = []
    for item, amount in ingredients.items():
        if resources[item]["amount"] < amount:
            lacking.append(item)
    return lacking
        
def collect_money():
    """Asks them for some coins"""
    print("Please insert coins.")
    total = 0.0
    
    quarters = int(input("how many quarters?: "))
    total += quarters * 0.25
    
    dimes = int(input("how many dimes?: "))
    total += dimes * 0.10
    
    nickles = int(input("how many nickles?: "))
    total += nickles * 0.05
    
    pennies = int(input("how many pennies?: "))
    total += pennies * 0.01
    
    return total

def enough_funds(funds, choice):
    """Determines if the given amount of money will cover the cost of the requested drink"""
    return funds >= MENU[choice]["cost"]

def change_due(funds, choice):
    """Calculates the amount of change due back for a certain drink and a given amount of money"""
    return funds - MENU[choice]["cost"]

def make_drink(choice):
    """Makes the drink and consumes the necessary resources"""
    for item, amount in ingredients(choice).items():
        resources[item]["amount"] -= amount

while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    
    # secret off command
    if choice == "off":
        break
        
    # hidden report command
    if choice == "report":
        report()
        continue

    # Check Resources Sufficient
    if lacking := enough(ingredients(choice)):
        print(f"Sorry there is not enough {lacking[0]}", end="")
        if len(lacking) > 2:
            for i in range(1, len(lacking) - 1):
                print(f", {lacking[i]}", end="")
        if len(lacking) > 1:
            print(f" or {lacking[-1]}")
        else:
            print()
        continue
    
    # Process Coins
    funds = collect_money()
    if not enough_funds(funds, choice):
        print("Sorry that's not enough money.  Money refunded.")
        continue
        
    # Check Transaction Successful?
    change = change_due(funds, choice)
    tendered = funds - change
    resources["money"]["amount"] += tendered
    if change:
        print(f"Here is ${change:.2f} in change.")
    else:
        print("No change back.")
    
    # Make Coffee
    make_drink(choice)
    print(f"Here is your {choice} ☕ Enjoy!")