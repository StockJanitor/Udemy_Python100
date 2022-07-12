# from calendar import c
# from pyrsistent import m
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


def load_resource(coffee):
    """input - type of coffee, output - resource amount"""
    w,mk,c,m=0,0,0,0
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
    global water, milk, coffee
    # action
    action = input("What would you like? ")
    if action in list_menu:

        # get amount of resources
        w,mk,c,m = load_resource(action)

        # reassign the new resources left
        water = water -w
        milk = milk-mk
        coffee = coffee-c

        #check resrouces
        if (water<0) or (milk<0) or (coffee<0):
            print("not enough resources")
            quit()
        
        else:
        # Process coins clause
            quarters =int(input("how many quaters ? "))
            dimes = int(input("how many dimes? "))
            nickles = int(input("how many nickles? "))
            pennies = int(input("how many pennies? "))
            total = quarters*.25 + dimes*.1 + nickles*.05 +pennies*.01

            if (total - money) >= 0:
                print("drink processed")

            else: 
                pass

    elif action == "off":
        quit()

    elif action == "report":
        print(f"water :{water}")
        print(f"milk :{milk}")
        print(f"coffee :{coffee}")
    
    else:
        print("invlaid command \n")
        machine()

    repeat= input("would you like to take action again? ")
    if repeat =="yes":
        machine()
    else:
        quit()

machine()
