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
}


class msg:
   ASK_FOR_SELECTION = "\nWhat would you like? "
   REPORT = "=" * 80 + "\nResources\n" + "=" * 80
   PRESS_ANY_KEY = "\nPress the enter key to return to prompt. "
   ITEM_NOT_IN_MENU = "\nSorry, the item is not in menu."
   ENTER_COINS = "\nPlease insert coins."
   ENTER_QUARTERS = "  How many quarters? "
   ENTER_DIMES = "  How many dimes? "
   PAY_OR_CANCEL = "\nPress 'p' to pay or 'enter' to cancel. "
   WELCOME_TO_MENU = "\nWelcome, this is our current menu."