customer = int(input("Insert Coin: "))
coke_price = 50
due_coin = [25, 10, 5]

while coke_price >= 0:
    if due_coin in customer:
        coke_price -= customer
    else:
        print("the machine accept only [25 ,10 ,5])
