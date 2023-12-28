customer = int(input("Insert Coin: "))
coke_price = 50
due_coin = [25, 10, 5]

while coke_price >= 0:
    for coin in customer:
        if due_coin in coin:
            coke_price -= customer
            customer = int(input("Insert Coin: "))
        else:
            print("the machine accept only [25 ,10 ,5]")
