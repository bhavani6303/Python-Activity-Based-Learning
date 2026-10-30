routes = [95, 120, 45]
bus_capacity = 40

for i in range(len(routes)):
    passengers = routes[i]
    buses = (passengers + bus_capacity - 1) // bus_capacity

    served = min(passengers, buses * bus_capacity)
    unserved = passengers - served

    print("Route", i + 1)
    print("Buses needed:", buses)
    print("Unserved passengers:", unserved)