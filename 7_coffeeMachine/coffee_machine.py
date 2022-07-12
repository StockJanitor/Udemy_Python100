from calendar import c
from pyrsistent import m
from coffee_data import MENU, resources

list_menu = ["espresso", "latte", "cappuccino"]

# input - espresso, latte, cappuccino, off, report

# if drink check resources

# if resources process coins, if enough coins process, else need more coin

# make more?

water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]

money = 0.00


def check_resource(coffe):
    """type of coffee, resources"""
    # conditions
    try:
        w = MENU[coffee]["ingredients"]["water"]
        mk = MENU[coffee]["ingredients"]["milk"]
        c = MENU[coffee]["ingredients"]["coffee"]
        m = MENU[coffee]["cost"]
    except:
        pass

    return w, mk, c, m


def machine():
    """run coffee machine"""

    # action
    action = input("What would you like? ")
    if action in list_menu:
        check_resource(action)

    elif action == "off":
        quit()
    elif action == "report":
        print()
    else:
        try:
            pass

        except:
            pass
