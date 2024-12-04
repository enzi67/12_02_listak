import random

numbers = [random.randint(-60, 100) for numero in range(50)]

print("10. Igaz-e, hogy a sorozat szigorúan monoton növekvő?")

monoton = True

for i in range(1, len(numbers)):
    if numbers[i] <= numbers[i - 1]:
        monoton = False
        break

if monoton:
    print("Igen, a sorozat szigorúan monoton növekvő.")
else:
    print("Nem, a sorozat nem szigorúan monoton növekvő.")

print("Alap lista:", numbers)
