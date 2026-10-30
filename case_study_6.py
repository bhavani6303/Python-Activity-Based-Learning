stock = {
    "Idli": 20,
    "Dosa": 15,
    "Rice": 10
}

price = {
    "Idli": 20,
    "Dosa": 40,
    "Rice": 50
}

sales = 0

orders = [("Idli", 3), ("Dosa", 2), ("Rice", 4)]

for item, quantity in orders:
    if quantity <= stock[item]:
        stock[item] -= quantity
        bill = price[item] * quantity
        sales += bill
        print(item, "Bill:", bill)
    else:
        print(item, "Not enough stock")

print("Total sales:", sales)
print("Remaining stock:", stock)