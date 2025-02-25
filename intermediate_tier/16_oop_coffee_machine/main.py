from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee = CoffeeMaker()
machine = MoneyMachine()
menu = Menu()
while True:
    order = input("What would you like? (espresso/latte/cappuccino)")
    if order.lower() == "off":
        exit()
    if order.lower() == "report":
        coffee.report()
    else:
        drink = menu.find_drink(order)
        if coffee.is_resource_sufficient(drink) and machine.make_payment(drink.cost):
            coffee.make_coffee(drink)
