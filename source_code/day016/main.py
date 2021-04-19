from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
maker = CoffeeMaker()
money = MoneyMachine()

print("Stock levels:")
print(maker.report())
print("\nProfit level:")
print(money.report())

print(f"What would you like to drink? {menu.get_items()}")

ordering = True
while ordering:
  selection = menu.find_drink(input())
  #drink = MenuItem(selection)
  if maker.is_resource_sufficient(selection):
    print("Good to go")
  else:
    print("Insufficient resources.")
    ordering = False
  
  payment = money.make_payment(selection.cost)

  if payment:
    maker.make_coffee(selection)
    print("Thank you and have a great day.")
    ordering = False
  else:
    print("Payment insufficient.")
    ordering = False