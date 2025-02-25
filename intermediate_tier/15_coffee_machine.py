resources = {"water": 100, "milk": 50, "coffee": 76, "money": 2.5}
recipe = {
    "espresso": {"water": 10, "milk": 20, "coffee": 10},
    "latte": {"water": 10, "milk": 10, "coffee": 5},
    "cappuccino": {"water": 200, "milk": 0, "coffee": 0},
}
price_list = {"espresso": 1, "latte": 1, "cappuccino": 1}


def process_coins():
    done = False
    total = 0
    coins = {"dollar": 1, "nickel": 0.25, "dime": 0.1, "penny": 0.01}
    while not done:
        coin_type = input("Type stop, or type coin_type (nickel,dime, dollar, penny)")
        if coin_type != "stop":
            total += coins[coin_type]
        else:
            done = True
    return total


def check_sufficient(order, resource):
    if resources[resource] < recipe[order][resource]:
        print(f"Sorry not enough {resource}")
        return False
    return True


def check_payment(payment, order):
    price = price_list[order]
    if payment < price:
        print("Not enough money")
        return False, None  # payment is just never added
    else:
        if payment > price:
            print(f"Here are ${round(payment-price, 2)} in change")
        return True, payment - price


while True:
    order = input("What would you like? (espresso/latte/cappuccino)")
    if order.lower() == "off":
        exit()
    if order.lower() == "report":
        print(f"water: {resources["water"]}ml")
        print(f"milk: {resources["milk"]}ml")
        print(f"coffee : {resources["coffee"]}g")
        print(f"money: ${resources["money"]}")
    else:
        order_ok = True
        for resource in recipe[order]:
            order_ok &= check_sufficient(order, resource)

        payment = process_coins()
        payment_sufficient, change = check_payment(payment, order)
        if order_ok and payment_sufficient:
            resources["money"] += payment - change
            for resource in recipe[order]:
                resources[resource] -= recipe[order][resource]
            print(f"Here is your {order}. Enjoy!")
