import database
from os import system
import math

currency_value = {
        'quarters': 25,
        'dimes': 10,
        'nickels': 5,
        'pennies': 1
    }

currency = {
        'quarters': 0,
        'dimes': 0,
        'nickels': 0,
        'pennies': 0
    }

def selection():
    return input("What would you like? (espresso/latte/cappuccino): ").lower()

def drink_check(drink):
    for i in database.MENU[drink]['ingredients']:
        if database.resources[i] < database.MENU[drink]['ingredients'][i]:
            print(f"Sorry, there is not enough {i}")
            return
    if payment(drink):
        for i in database.MENU[drink]['ingredients']:
            database.resources[i] -= database.MENU[drink]['ingredients'][i]
        print(f"Here is your {drink}. Enjoy!")

def payment(drink):
    money_paid = {}
    total_paid = 0
    change = 0
    global currency
    print(f"Please insert coins.")
    for coin in currency_value:
        money_paid[coin] = (int(input(f"How many {coin}?: ")))
        total_paid += (money_paid[coin] * currency_value[coin])
    change = (total_paid - (database.MENU[drink]['cost'] * 100))
    if change >= 0:
        print(f"Here is your ${(change/100):.2f} change.")
        for coin in money_paid:
            currency[coin] += money_paid[coin]
            returned = math.floor((change)/currency_value[coin])
            currency[coin] -= returned
            change -= returned * currency_value[coin]
        return True
    else:
        print(f"Sorry, that's not enough money. Money refunded.")
        return False

def report():
    sum = 0
    for i in database.resources:
        print(f"{i.capitalize()}: {database.resources[i]}ml")
    for i in currency:
        sum += ((currency[i] * currency_value[i])/100)
    print(f"Money: ${sum:.2f}")
    print(currency)

while (select:= selection()) != 'off':
    report() if select == 'report' else drink_check(select)