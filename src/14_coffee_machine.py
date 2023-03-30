import random


def ask_coffee():
    selected_option = input(
        "What would you like to drink? (espresso/latte/cappuccino): ").lower()

    options_and_prices = {
        "espresso": 1.5,
        "latte": 2.5,
        "cappuccino": 3.0
    }

    price = options_and_prices[selected_option]

    print(f"That will be ${price}.")
    print("Please insert some coins.")

    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))

    total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01

    print(total)

    if total < price:
        print("Sorry that's not enough money. Money refunded.")
        return

    change = round(total - price, 2)

    if (change > 0):
        print(f"Here is ${change} in change.")

    print(f"Here is your {selected_option} ☕. Enjoy!")


while (True):
    ask_coffee()

    ask_again = input("Press off? (y/n) ").lower()

    if ask_again == "y":
        break
