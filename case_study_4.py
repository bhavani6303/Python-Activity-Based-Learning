transactions = [
    (101, 500, "Credit"),
    (102, 300, "Debit"),
    (101, 200, "Credit"),
    (103, -100, "Debit")
]

ids = []

for t in transactions:
    if t[0] in ids:
        print("Duplicate transaction ID:", t[0])
    else:
        ids.append(t[0])

    if t[1] < 0:
        print("Invalid amount:", t[1])

print("Audit completed")