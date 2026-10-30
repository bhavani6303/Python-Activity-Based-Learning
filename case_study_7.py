books = [
    ("B101", 5),
    ("B102", 2),
    ("B103", 7)
]

fine_per_day = 5
total_fine = 0

for book, days_late in books:
    fine = days_late * fine_per_day
    total_fine += fine

    print("Book:", book)
    print("Fine:", fine)

print("Total fine:", total_fine)