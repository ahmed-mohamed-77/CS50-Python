coke_price = 50
due_coins = [25, 10, 5]

print(f"Amount Due: {coke_price}")
while coke_price > 0:
    customer_coin = int(input("Insert Coin: "))

    if customer_coin in due_coins:
        coke_price -= customer_coin
        print(f"Amount Due: {coke_price}")
print(f"Change Owed: {coke_price}")


