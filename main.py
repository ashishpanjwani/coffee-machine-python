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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO: 1. Print the Report
def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


# TODO: 2. Check if resource is sufficient
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


# TODO: 3. Insert the coins
def insert_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01

    return total


# TODO: 4. Check if transaction completed successfully
def is_transaction_successful(money, coffee_cost):
    if money >= coffee_cost:
        balance = round(money - coffee_cost, 2)
        if balance > 0:
            print(f"Here is ${balance} in change.")
        global profit
        profit += coffee_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


# TODO: 5. Make the Coffee
def make_coffee(coffee, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your latte ☕. Enjoy!")


is_on = True

while is_on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == "off":
        is_on = False
    elif user_input == "report":
        print_report()
    else:
        drink = MENU[user_input]
        if is_resource_sufficient(drink['ingredients']):
            money_received = insert_coins()
            if is_transaction_successful(money_received, drink['cost']):
                make_coffee(user_input, drink['ingredients'])
