import random

numbers = [random.randint(-60, 100) for _ in range(50)]

print("2. Írjuk ki az utolsó 5-tel vagy 7-tel osztható szám indexét!")

# Az utolsó 5-tel vagy 7-tel osztható szám indexének keresése
utolso_oszthato_index = next((i for i in range(len(numbers) - 1, -1, -1) if numbers[i] % 5 == 0 or numbers[i] % 7 == 0), None)

# Kiírás
if utolso_oszthato_index is not None:
    print(f"Az utolsó 5-tel vagy 7-tel osztható szám indexe: {utolso_oszthato_index}")
else:
    print("Nincs 5-tel vagy 7-tel osztható szám a listában.")

# A generált lista megjelenítése
print("Alap lista:", numbers)
