from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cm = CoffeeMaker()
mm = MoneyMachine()
menu = Menu()

is_on = True

while True:
	user_selection = input(f"What would you like? {menu.get_items()}: ")
	if user_selection == "report":
		cm.report()
		mm.report()
		continue
	elif user_selection == "off":
		print("Powering Down...")
		exit()
	elif user_selection not in menu.get_items().split('/'):
		print("Invalid selection. Please try again...")
		continue
	else:
		item = menu.find_drink(user_selection)
		if cm.is_resource_sufficient(item):
			if mm.make_payment(item.cost):
				cm.make_coffee(item)
