from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def app():
    menu = Menu()
    moneymachine = MoneyMachine()
    coffeemaker = CoffeeMaker()

    running = True
    menu_items = menu.get_items().split('/')

    while running:
        user_selection = input(f"\nWhat would you like? {menu.get_items()} :")

        if user_selection == "report":
            coffeemaker.report()
            moneymachine.report()
        elif user_selection == "exit" or user_selection == "off":
            running = False
        elif user_selection in menu_items:
            order = menu.find_drink(user_selection)
            if coffeemaker.is_resource_sufficient(order):
                if moneymachine.make_payment(order.cost):
                    coffeemaker.make_coffee(order)
                
        else:
            print("I didn't understand that. Please try again")

app()






