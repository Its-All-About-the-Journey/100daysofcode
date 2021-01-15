import os

from coffee import MENU, msg, resources

CLEAR = "cls" if os.name == 'nt' else "clear"

def update_prompt():
    pass

def prompt():
    # Get the user's input

    return input(f"{ msg.ASK.format( menu() )}")

def print_report():
    # Print current resource values
    #
    # Resources: from coffee import resources
    pass

def menu() -> str:
    # Return menu based on current resources
    pass

def currency_balance():
    # Return the currency balance
    #
    # - A negative number means insuffient currency
    # - A positive number means currency owed
    pass

def register():
    # Prompt user for cash
    #
    # While short_change
    #    prompt for remaining balance or eject to cancel
    #
    # Coin inputs: quarter, dime, nickle, and penny
    pass

def process_order():
    # Update inventory of resources
    #
    # Resources: from coffee import resources
    pass

def run():
    # Brains of the coffee machine
    while True:

        user_selection = prompt()

        if user_selection == 'off':
            break


if __name__ == "__main__":
    run()
