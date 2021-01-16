from coffee_menu import Menu
from coffee_maker import CoffeeMaker
from coffee_money import MoneyMachine

# the top of the line coffee maker
turbo_delux_9000 = CoffeeMaker()

# the top of the...ok, bottom of the line pos system
cash_register = MoneyMachine()

# our cute hand drawn chalkboard menu with only three items on it
the_menu = Menu()

# run the machine until it's turned off
while True:
    
    # ask the customer what they want today
    choice = input(f"What would you like? ({the_menu.get_items()}): ")
    
    # system menu: turn off
    if choice == "off":
        break
        
    # system menu: print report
    if choice == "report":
        turbo_delux_9000.report()
        cash_register.report()
        continue
        
    # let's make sure we even sell this drink.  these karen's and their damn demands on us!
    if not (drink := the_menu.find_drink(choice)):
        continue

    # let's make sure we can even make this drink...scotty!  where's the milk?
    if not turbo_delux_9000.is_resource_sufficient(drink):
        continue

    # process the payment for the drink, but only accept coins, because we're weird and cool and stuff
    if not cash_register.make_payment(drink.cost):
        continue

    # make the drink and hand it to the customer....careful!  don't spill it.  it's very hot!
    turbo_delux_9000.make_coffee(drink)