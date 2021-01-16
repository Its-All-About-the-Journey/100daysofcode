from copy import deepcopy
import os

from coffee import MENU, msg, resources

CLEAR = "cls" if os.name == 'nt' else "clear"

def update_prompt():
    pass

def prompt() -> None:
    # Get the user's input
    print( menu() )
    return input(f"{msg.ASK_FOR_SELECTION}")

def print_report() -> None:
    # Print current resource values
    
    os.system(CLEAR)
    print(msg.REPORT)
    print(f"{'Water':<8}  {resources['water']:>5} ml")
    print(f"{'Milk':<8}  {resources['milk']:>5} ml")
    print(f"{'Coffee':<8}  {resources['coffee']:>5} g")
    print(f"{'Money':<8}  ${resources['money']:>.2f}")

    # Await on user input so he can view report
    input(msg.PRESS_ANY_KEY)

def menu() -> str:
    # Return menu based on current resources
    menu = "Here is our current menu:"

    menu_items = dict()

    # Build menu based on inventory availability
    for item in MENU:
        add_item = True
        for key, value in MENU[item]["ingredients"].items():
            if value > resources[key]:
                add_item = False
                break

        if add_item:
            menu = menu + f"\n   {item:<10} - $ {MENU[item]['cost']:.2f}"

    return menu


def currency_balance():
    # Return the currency balance
    #
    # - A negative number means insuffient currency
    # - A positive number means currency owed
    pass

def register(amount: float) -> bool:
    # Prompt user for cash
    #
    quarters = dimes = registered_amount = 0
    owes = amount

    while input(msg.PAY_OR_CANCEL) == 'p':
        os.system(CLEAR)
        print(f"Registered amount is: $ {registered_amount:.2f}")
        print(f"Amount needed $ {owes:.2f}")        
        print(msg.ENTER_COINS)

        quarters = int( input(msg.ENTER_QUARTERS) )
        
        dimes = int( input(msg.ENTER_DIMES) )

        registered_amount +=  quarters * .25 + dimes * .10

        owes = amount - registered_amount

        if owes > 0:
            print(f"\nYou are short, you still need $ {owes:.2f}")
        else:
            return True 
    
    return False



def process_order():
    # Update inventory of resources
    #
    # Resources: from coffee import resources
    pass

def run():
    # Brains of the coffee machine

    # Initial live menu and resources
    menu = deepcopy(MENU)
    resources['money'] = 0

    while True:
        os.system(CLEAR)
        user_selection = prompt()

        if user_selection == 'off':
            # Shut off system
            break
        
        elif user_selection == 'report':
            # Print resource report
            print_report()
        
        else:
            # is selection valid
            if user_selection in menu.keys():
                # register purchase
                amount = menu[user_selection]['cost']

                if register(amount):
                    print('yes')
                    # eject change
                    # process order

                input(msg.PRESS_ANY_KEY)
            else:
                print(msg.ITEM_NOT_IN_MENU)
                input(msg.PRESS_ANY_KEY)
                continue



if __name__ == "__main__":
    run()
