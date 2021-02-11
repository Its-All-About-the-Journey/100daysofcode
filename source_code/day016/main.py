from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeeMenu = Menu()
paymentProcessor = MoneyMachine()
machine = CoffeeMaker()

while (choice:= input(f"What would you like? {coffeeMenu.get_items()} ")) != 'off':
    if choice == 'report':
        machine.report()
        paymentProcessor.report()
    else:
        if (drink := coffeeMenu.find_drink(choice)) != None:
            if machine.is_resource_sufficient(drink) and paymentProcessor.make_payment(drink.cost):
                machine.make_coffee(drink)