import random

numbers = [random.randint(-60, 100) for szam in range(50)]

print("6. Hány 18-cal osztható szám található a sorozatban?")

count = sum(1 for num in numbers if num % 18 == 0)

print(f"Az 18-cal osztható számok száma: {count}")

print("Alap lista:", numbers)
