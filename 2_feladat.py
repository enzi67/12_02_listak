import random

numbers = [random.randint(-60, 100) for num in range(50)]

print("2. Írjuk ki az utolsó 5-tel vagy 7-tel osztható szám indexét!")

utolso_oszthato_index = next((i for i in range(len(numbers) - 1, -1, -1) if numbers[i] % 5 == 0 or numbers[i] % 7 == 0), None)

if utolso_oszthato_index is not None:
    print(f"Az utolsó 5-tel vagy 7-tel osztható szám indexe: {utolso_oszthato_index}")
else:
    print("Nincs 5-tel vagy 7-tel osztható szám a listában.")

print("Alap lista:", numbers)
