import random

numbers = [random.randint(-60, 100) for _ in range(50)]

print("8. Írjuk ki a sorozatban található 17-tel vagy 18-cal osztható számok négyzetét!")

for num in numbers:
    if num % 17 == 0 or num % 18 == 0:
        print(f"A szám: {num}, négyzete: {num ** 2}")

print("Alap lista:", numbers)
