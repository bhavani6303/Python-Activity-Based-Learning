prepared = [100, 120, 150]
served = [80, 100, 120]

for i in range(len(prepared)):
    waste = prepared[i] - served[i]
    percentage = (waste / prepared[i]) * 100

    print("Day", i + 1)
    print("Food wasted:", waste)
    print("Waste percentage:", percentage, "%")