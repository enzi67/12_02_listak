import random

numbers = [random.randint(-60, 100) for num in range(50)]

print("3. Írjuk ki az első 3-mal és 7-tel osztható szám indexét!")

for i, num in enumerate(numbers):
    if num % 3 == 0 and num % 7 == 0:
        print(f"Az első 3-mal és 7-tel osztható szám indexe: {i}")
        break
else:
    print("Nincs 3-mal és 7-tel osztható szám a listában.")

print("Alap lista:", numbers)
