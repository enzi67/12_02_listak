import random

numbers = [random.randint(-60, 100) for _ in range(50)]

print("7. Mennyi a sorozatban található egyik legkisebb szám indexe?")

min_value = numbers[0]
min_index = 0

for i in range(1, len(numbers)):
    if numbers[i] < min_value:
        min_value = numbers[i]
        min_index = i

print(f"A legkisebb szám: {min_value}")
print(f"A legkisebb szám indexe: {min_index}")

print("Alap lista:", numbers)
