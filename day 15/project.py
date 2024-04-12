# COFFE MACHINE PROJECT

from random import choice
from data import MENU, resources, logo
from replit import clear     

def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def start_machine():
    print(logo)
    choice = str(input("What would you like? (espresso/latte/cappuccino): ")).strip().lower()
    return choice

def check_ingredients():
    if choice == "espresso":
        resources["water"] = resources["water"] - items["water"]
        resources["coffee"] = resources["coffee"] - items["coffee"]
    else:
        resources["water"] = resources["water"] - items["water"]
        resources["milk"] = resources["milk"] - items["milk"]
        resources["coffee"] = resources["coffee"] - items["coffee"]
    return resources

lucro = 0
is_off = False
while not is_off:
    choice = start_machine()
    if choice == "off":
        print("Turning off the machine.")
        is_off = True
    elif choice == "report":
        print(f"Water: {resources['water']} mL")
        print(f"Milk: {resources['milk']} mL")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Money: $ {lucro}")
    elif choice in MENU:
        flavor = MENU[choice] # Picks the flavor in the dict
        items = flavor["ingredients"] # What it need
        rest = check_ingredients()
        if rest["water"] < 0 or rest["milk"] < 0 or rest["coffee"] < 0:
            print("Sorry there is not enough ingredients.")
        else:
            profit = process_coins()
            price = flavor["cost"]
            change = profit - price
            lucro += price
            if change > 0:
                print(f"Your change is $ {change:.2f}.")
                print(f"Here is your {choice}. Enjoy!")
            else:
                print("Sorry. You don't have enough money.")
    else:
        clear()
        print("Invalid input. Try again!")
