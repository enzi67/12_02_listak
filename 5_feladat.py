import random

numbers = [random.randint(-60, 100) for _ in range(50)]

print("5. Van-e a sorozatban olyan szám, amelyik 1 és 10 közé esik?")

found = False

for num in numbers:
    if 1 <= num <= 10:
        found = True
        break

if found:
    print("Igen, van olyan szám, amely 1 és 10 közé esik.")
else:
    print("Nem, nincs olyan szám, amely 1 és 10 közé esik.")

print("Alap lista:", numbers)
