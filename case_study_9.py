production = [
    [100, 5],
    [200, 10],
    [150, 30]
]

limit = 10

for i in range(len(production)):
    total = production[i][0]
    defective = production[i][1]

    percentage = (defective / total) * 100

    print("Batch", i + 1)
    print("Defect percentage:", percentage, "%")

    if percentage > limit:
        print("Quality threshold exceeded")