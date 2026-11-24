from menu import Menu,MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#TODO 1: Print report.
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

#TODO 2: Check resources sufficient.
is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like ({options})")

    if choice == "off":
        is_on = False
    elif choice == "report":
        coffe_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice) # drink object ban gye MenuItem object
        if coffe_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffe_maker.make_coffee(drink)



#TODO 3: Process Coins.
#TODO 4: Check transaction successful.
#TODO 5: Make Coffe.