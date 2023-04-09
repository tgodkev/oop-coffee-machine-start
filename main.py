from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

print("Welcome to the Coffee Machine")

while True:
    order = input("What would you like to order? (espresso/latte/cappuccino/stop): ")
    
    if order == "stop":
        break

    if order == "espresso":
        menu_item = menu.find_drink("espresso")
        print(f'You ordered {menu_item.name} for {menu_item.cost} dollars')
        if money_machine.make_payment(menu_item.cost) == True:
            coffee_maker.make_coffee(menu_item)

    if order == "latte":
        menu_item = menu.find_drink("latte")
        print(f'You ordered {menu_item.name} for {menu_item.cost} dollars')
        if money_machine.make_payment(menu_item.cost) == True:
            coffee_maker.make_coffee(menu_item)

    if order == "cappuccino":
        menu_item = menu.find_drink("cappuccino")
        print(f'You ordered {menu_item.name} for {menu_item.cost} dollars')
        if money_machine.make_payment(menu_item.cost) == True:
            coffee_maker.make_coffee(menu_item)

    if order == 'report':
        money_machine.report()
