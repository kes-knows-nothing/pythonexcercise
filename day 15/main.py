MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "ingredients": {
        "water": 300,
        "milk": 200,
        "coffee": 100
    },
    "Money": 0.0
}

order_ready = True

# 돈 묻기

def ask_money():
    print("Please insert coins")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    sum_of_money = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return sum_of_money

## 재료가 부족한지 체크


def enough_res():

    if resources["ingredients"]["water"] >= MENU[ORDER]["ingredients"]["water"] and resources["ingredients"]["milk"] >= MENU[ORDER]["ingredients"]["milk"] and resources["ingredients"]["coffee"] >= MENU[ORDER]["ingredients"]["coffee"]:
        True

    else:
        for key in MENU[ORDER]["ingredients"]:
            if resources["ingredients"][key] < MENU[ORDER]["ingredients"][key]:
                print(f"Sorry there is not enough {key}")
                return False
        return True



# 돈 계산

def calc():
    if don >= MENU[ORDER]["cost"]:
        change = don - MENU[ORDER]["cost"]
        print(f"Here is ${change} in change.")
        print(f"Here is your {ORDER}. Enjoy!")
        make_coffee()

    else:
        print("Sorry that's not enough money. Money refunded.")
        order_ready


# make coffee
def make_coffee():
    """select menu and make drink and show lefts"""

    for key in MENU[ORDER]["ingredients"]:
        resources["ingredients"][key] -= MENU[ORDER]["ingredients"][key]
    resources["Money"] = resources["Money"] + MENU[ORDER]["cost"]
    return resources

# 정리




while order_ready:
    ORDER = input("What would you like? (espresso/latte/cappuccino): ")
    if ORDER == "off":
        order_ready = False
    elif ORDER == "report":
        print(f'Water: {resources["ingredients"]["water"]}ml\nMilk: {resources["ingredients"]["milk"]}ml\nCoffee: {resources["ingredients"]["coffee"]}g\nMoney: ${resources["Money"]}')
        order_ready
    elif ORDER == "espresso" or ORDER == "latte" or ORDER == "cappuccino":
        enough_res()
        don = round(ask_money(), 2)
        calc()








