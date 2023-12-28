coke_price = 50
due_coins = [25, 10, 5]

while coke_price > 0:
    customer_coin = int(input("Insert Coin: "))

    if customer_coin in due_coins:
        coke_price -= customer_coin
    else:
        print("The machine only accepts coins of [25, 10, 5]")

print("Enjoy your coke!")
