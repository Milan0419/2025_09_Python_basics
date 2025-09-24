import random

szam = random.randint(1, 3)
x = int(input("Írj be egy számot 1 és 3 között: "))


if x == szam:
    print(f"A válasz helyes, mert a random szám a(z) {szam}")
else:
    print(f"A válasz helytelen, a helyes válasz a(z) {szam}")