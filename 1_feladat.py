import random
import math

numbers = [random.randint(-60, 100) for num in range(50)]

print("1. Mennyi a sorozatban található számok szorzata?")
product_of_numbers = math.prod(numbers)
print("A számok szorzata:", product_of_numbers)

print("Alap lista:", numbers)
