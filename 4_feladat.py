import random

numbers = [random.randint(-60, 100) for numim in range(50)]

print("4. Igaz-e, hogy minden szám negatív?")

minden_negativ = True

for num in numbers:
    if num >= 0:
        minden_negativ = False
        break

if minden_negativ:
    print("Igen, minden szám negatív. Nincs pozitív szám a listában.")
else:
    print("Nem minden szám negatív. Pozitív szám is van a listában.")

print("Alap lista:", numbers)
