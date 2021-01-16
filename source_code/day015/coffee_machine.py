from copy import deepcopy
import os

from coffee import MENU, msg, resources

CLEAR = "cls" if os.name == 'nt' else "clear"

def prompt(live_menu) -> None:
    print_menu(live_menu)

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

def print_menu(menu) -> None:
    print(msg.WELCOME_TO_MENU + '\n')

    for item in menu:
        print(f"   {item:<10} - $ {menu[item]['cost']:.2f}")

def update_menu() -> dict:

    menu = dict()

    # Build menu based on resource availability
    for item in MENU:
        add_item = True

        for key, value in MENU[item]["ingredients"].items():
            if value > resources[key]:
                add_item = False
                break

        if add_item:
            menu[item] = deepcopy(MENU[item])
    
    return menu

def register(amount: float) -> bool:
    # Prompt user for cash
    quarters = dimes = registered_amount = 0
    owes = amount

    while input(msg.PAY_OR_CANCEL) == 'p':
        os.system(CLEAR)
        print(f"Registered amount is: $ {registered_amount:.2f}")
        print(f"Amount needed $ {owes:.2f}")        
        print(msg.ENTER_COINS)

        try:
            quarters = int( input(msg.ENTER_QUARTERS) )
            dimes = int( input(msg.ENTER_DIMES) )
        except ValueError:
            # Lazy validation
            pass

        registered_amount +=  quarters * .25 + dimes * .10

        owes = amount - registered_amount

        if owes > 0:
            print(f"\nYou are short, you still need $ {owes:.2f}")
        else:
            change = registered_amount - amount
            print(f"\nYou have $ {change:.2f} change.")
            return True
    
    # Order cancelled return money
    print(f"\nYou have $ {registered_amount:.2f} change.")

    return False

def process_order(resource: dict, menu: dict, item: str) -> None:
    # Update resources
    for ingredient in menu[item]["ingredients"]:
        resources[ingredient] -= menu[item]["ingredients"][ingredient]
    
    # Update money
    resources["money"] += menu[item]["cost"]

def run():
    # Brains of the coffee machine

    # Initial money resources
    resources['money'] = 0

    while True:
        # Update live menu
        live_menu = update_menu()

        if not live_menu:
            # Shut off, no items to offer
            print_report()
            print("\nOut of Stock")
            break

        os.system(CLEAR)
        user_selection = prompt(live_menu)

        if (user_selection == 'off'):
            # Shut off system
            break
        
        if user_selection == 'report':
            # Print resource report
            print_report()
        
        elif user_selection in live_menu.keys():
            # User selection is in live menu

            # register purchase
            amount = live_menu[user_selection]['cost']

            if register(amount):
                # User paid, process order
                process_order(resources, MENU, user_selection)
                print("\nThank you for the order.")
                print(f"Here is your {user_selection}.")
        
            input(msg.PRESS_ANY_KEY)

        else:
            # Invalid selection
            print(msg.ITEM_NOT_IN_MENU)
            input(msg.PRESS_ANY_KEY)

if __name__ == "__main__":
    run()
