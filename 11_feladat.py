import random

numbers = [random.randint(-60, 100) for _ in range(50)]

print("11. Válogassuk ki két listába a páros és a páratlan számokat!")

paros_szamok = []
paratlan_szamok = []

for num in numbers:
    if num % 2 == 0:
        paros_szamok.append(num)
    else:
        paratlan_szamok.append(num)

print(f"Páros számok: {paros_szamok}")
print(f"Páratlan számok: {paratlan_szamok}")

print("Alap lista:", numbers)
