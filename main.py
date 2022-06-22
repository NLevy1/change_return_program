money_dict = {
    'Fifties': 0,
    'Twenties': 0,
    'Tens': 0,
    'Fives': 0,
    'Twos': 0,
    'Ones': 0,
    'Fifty cents': 0,
    'Twenty cents': 0,
    'Ten_cents': 0,
    'Five_cents': 0,
    'Two_cents': 0,
    'One_cents': 0
}

money_list = list(money_dict.keys())
amount_list = [50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
calculating = True

def set_price_and_money(payment_commenced=False, price=0, money=0):
    price_of_item = price
    money_given = money
    paid = payment_commenced

    while not paid:
        print("Welcome to the change return program!")
        while not price_of_item:
            try:
                price_of_item = float(input("What is the price of the item?  "))
            except ValueError:
                print("That's not a valid amount.")
        while not money_given:
            try:
                money_given = float(input("How much money is given?  "))
            except ValueError:
                print("That's not a valid amount.")

        if money_given - price_of_item < 0:
            print("That's not enough money.")
            money_given = 0
        else:
            paid = True

    return money_given - price_of_item


def calculate_change(change):
    for amount in amount_list:
        while round(change, 2) >= amount:
            change -= amount
            money_dict[money_list[amount_list.index(amount)]] += 1

def what_to_give_back():
    print("\nThe change is as follows: \n")
    for k, v in money_dict.items():
        print(f"{k}: {v}")



if __name__ == "__main__":
    calculate_change(set_price_and_money())
    what_to_give_back()
