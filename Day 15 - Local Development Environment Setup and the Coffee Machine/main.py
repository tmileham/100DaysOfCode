from menu import MENU, resources, profit, coins

def process_coins(chosen_drink):
    """Request payment from user based on selected drink and add to profit"""
    
    global profit
    cost = chosen_drink['cost']
    coins_inserted_value = 0

    print(f"The price is ${cost}")
    print("Please insert coins.")

    for coin, value in coins.items():
        coins_inserted_value += value * int(input(f"How many {coin}'s :"))

    result = abs(round(cost - coins_inserted_value, 2))

    if coins_inserted_value >= cost:
        print(f"\nYour change: ${result}")
        profit += cost
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
    print(f"Profit: ${profit}")

def check_resources(chosen_drink,resources):
    """Checks if enough resources avaliable for the drink. Returns True or False"""

    # drink_ingredients = chosen_drink['ingredients']
     
    for ingredient,value in chosen_drink.items():
        if value > resources[ingredient]:
            print(f"Sorry, there isn't enough {ingredient}")
            return False
    return True


def make_drink(drink):
    """ Function which creates the coffee for the user. 
    Also, deducts the ingredients from the avalaible resources"""

    print(f"Here's your {drink} ☕")

    for key, values in MENU[drink]['ingredients'].items():       
        resources[key] = resources[key] - values


def print_menu():
    """prints drinks menu"""
    print("\nThe drinks on our menu are: ")
    for drink in MENU:
        print(f"\t{drink}")


def main_menu():
    """Function used to create the main menu functionality"""

    machine_running = True
    print("Welcome to Costya Coffee")


    def select_drink():
        """Functions to tidy up readibility for function calls required for for drink selection"""
        if user_selection in MENU.keys():
            if check_resources(MENU[user_selection]['ingredients'],resources):
                if(process_coins(MENU[user_selection])):
                    make_drink(user_selection)
                else:
                    print(f"Sorry not enough money. Money refunded")
            else:
                print(f"Please select a different drink")
        else:
            print(f"Unable to find that drink on the menu. Please try again")        

    while machine_running:
        user_selection = input("\nWhat would you like? (expresso/latte/cappuccino): ").lower()
        if user_selection == "report":
            print_resource_report()
        elif user_selection == "exit" or user_selection == "off":
            machine_running = False
        elif user_selection == "menu":
            print_menu()
        else:
            select_drink()

main_menu()