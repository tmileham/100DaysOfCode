from menu import MENU, resources, coins

# Pyhawkz
def process_coins(chosen_drink):
    """Request payment from user"""
    total_coin_value = 0
    cost = chosen_drink['cost']

    for coin, value in coins.items():
        total_coin_value += value * int(input(f"How many {coin}'s :"))

    result = abs(round(cost - total_coin_value, 2))

    if total_coin_value > cost:
        print(f"\nYour change: ${result}")
        return True
    else:
        print(f"\nYou're short by ${result}")
        return False


def print_resource_report():
    """prints resource quantity report"""
    for item, amount in resources.items():
        if item == "water" or item == "milk":
            print(f"{item.title()} - {amount}ml remaining")
        elif item == "coffee":
            print(f"{item.title()} - {amount}mg remaining")
        else:
            print(f"{item.title()} - ${amount}")




def check_resources(chosen_drink,resources):
    """Checks if enough resources avaliable for the drink. Returns True or False"""

    drink_ingredients = chosen_drink['ingredients']
     
    for ingredient,value in drink_ingredients.items():
        if value > resources[ingredient]:
            print(f"Sorry, there isn't enough {ingredient}")
            return False
    return True


def make_drink(drink):
    global resources
   
    for key, values in drink['ingredients'].items():
        #print(f"drink Key: {key}")
        #print(f"drink Values: {values}")
        
        resources[key] = resources[key] - values
        
    
    print(f"Here's your {drink} ☕")


def print_menu():
    """prints drinks menu"""
    print("\nThe drinks on our menu are: ")
    for drink in MENU:
        print(f"\t{drink}")




def main_menu():
    machine_running = True
    print("Welcome to Costya Coffee")

    while machine_running:
        user_selection = input("\nWhat would you like? (expresso/latte/cappuccino): ").lower()

        if user_selection == "report":
            print_resource_report()
        elif user_selection == "exit" or user_selection == "off":
            machine_running = False
        elif user_selection == "menu":
            print_menu()
        else:
            if user_selection in MENU.keys():
                if check_resources(MENU[user_selection],resources):
                    if(process_coins(MENU[user_selection])):
                        make_drink(MENU[user_selection])
                    else:
                        print(f"Sorry not enough money. Money refunded")
                else:
                    print(f"Please select a different drink")
            else:
                print(f"Unable to find that drink on the menu. Please try again")

main_menu()