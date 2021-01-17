from copy import deepcopy
import os

from coffee import MENU, msg, resources

CLEAR = "cls" if os.name == 'nt' else "clear"

class CoffeeMachine:

    def __init__(self):
        self.live_menu = deepcopy(MENU)
        self.resources = deepcopy(resources)
        self.resources['money'] = 0

    def prompt(self) -> str:
        self.print_menu()

        return input(f"{msg.ASK_FOR_SELECTION}")

    def print_report(self) -> None:
        # Print current resource values
        os.system(CLEAR)
        print(msg.REPORT)
        print(f"{'Water':<8}  {self.resources['water']:>5} ml")
        print(f"{'Milk':<8}  {self.resources['milk']:>5} ml")
        print(f"{'Coffee':<8}  {self.resources['coffee']:>5} g")
        print(f"{'Money':<8}  ${self.resources['money']:>.2f}")

        # Await on user input so he can view report
        input(msg.PRESS_ANY_KEY)

    def print_menu(self) -> None:
        print(msg.WELCOME_TO_MENU + '\n')

        for item in self.live_menu:
            print(f"   {item:<10} - $ {self.live_menu[item]['cost']:.2f}")

    def update_menu(self) -> None:
        items_to_pop =  list()

        # update menu based on resource availability
        for item in self.live_menu:
            for key, value in self.live_menu[item]["ingredients"].items():
                if value > self.resources[key]:
                    items_to_pop.append(item)
                    break
        
        # Remove items from menu
        for item in items_to_pop:
            del self.live_menu[item]
        
    def register(self, amount: float) -> bool:
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

    def process_order(self, item: str) -> None:
        # Update resources
        for ingredient in self.live_menu[item]["ingredients"]:
            self.resources[ingredient] -= self.live_menu[item]["ingredients"][ingredient]
        
        # Update money
        self.resources["money"] += self.live_menu[item]["cost"]

    def run(self) -> None:
        # Brains of the coffee machine

        while True:
            # Update live menu
            self.update_menu()

            if not self.live_menu:
                # Shut off, no items to offer
                self.print_report()
                print("\nOut of Stock")
                break

            os.system(CLEAR)
            user_selection = self.prompt()

            if (user_selection == 'off'):
                # Shut off system
                break
            
            if user_selection == 'report':
                # Print resource report
                self.print_report()
            
            elif user_selection in self.live_menu.keys():
                # User selection is in live menu

                # register purchase
                amount = self.live_menu[user_selection]['cost']

                if self.register(amount):
                    # User paid, process order
                    self.process_order(user_selection)
                    print("\nThank you for the order.")
                    print(f"Here is your {user_selection}.")
            
                input(msg.PRESS_ANY_KEY)

            else:
                # Invalid selection
                print(msg.ITEM_NOT_IN_MENU)
                input(msg.PRESS_ANY_KEY)

