seats = [
    [101, 102, 103],
    [104, None, 106],
    [107, 102, 109]
]

students = []

for row in seats:
    for seat in row:
        if seat is None:
            print("Empty seat")
        elif seat in students:
            print("Duplicate roll number:", seat)
        else:
            students.append(seat)

print("Seating validation completed")