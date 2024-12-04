"""Generáljunk le 50 db, -60 és 100 közötti véletlen számot (az input txt-hez hasonlóan, de természetesen listába rakva),
majd a következő feladatokat oldjuk meg.
Minden feladat előtt a program írja ki a feladat sorszámát! 
1. Mennyi a sorozatban található számok szorzata? 
2. Írjuk ki az utolsó 5-tel vagy 7-tel osztható szám indexét! 
3. Írjuk ki az első 3-mal és 7-tel osztható szám indexét! 
4. Igaz-e, hogy minden szám negatív? 
5. Van-e a sorozatban olyan szám, amelyik 1 és 10 közé esik? 
6. Hány 18-cal osztható szám található a sorozatban? 
7. Mennyi a sorozatban található egyik legkisebb szám indexe? 
8. Írjuk ki a sorozatban található 17-tel vagy 18-cal osztható számok négyzetét! 
9. Van-e a sorozatban olyan negatív szám, amelynek az összes szomszédja pozitív?
10. Igaz-e, hogy a sorozat szigorúan monoton növekvő?
11. Válogassuk ki két listába a páros és a páratlan számokat!"""

import random

numbers = [random.randint(-60, 100) for num in range(50)]

print("Lista:", numbers)
