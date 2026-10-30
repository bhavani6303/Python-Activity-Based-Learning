expenses = [
    [1000, 2000, 1500],
    [1200, 1800, 1000],
    [2000, 2500, 1500]
]

for i in range(len(expenses)):
    total = sum(expenses[i])
    average = total / len(expenses[i])

    print("Branch", i + 1)
    print("Total expense:", total)
    print("Average expense:", average)
     