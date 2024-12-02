import random

numbers = [random.randint(-60, 100) for _ in range(50)]

print("9. Van-e a sorozatban olyan negatív szám, amelynek az összes szomszédja pozitív?")

talált = False

for i in range(1, len(numbers) - 1):
    if numbers[i] < 0 and numbers[i - 1] > 0 and numbers[i + 1] > 0:
        talált = True
        break

if talált:
    print("Van olyan negatív szám, amelynek az összes szomszédja pozitív.")
else:
    print("Nincs olyan negatív szám, amelynek az összes szomszédja pozitív.")

print("Alap lista:", numbers)
