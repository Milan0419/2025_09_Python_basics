import random

szam = random.randint(1, 5)
x = int(input("Írj be egy számot 1 és 5 között: "))


if x == szam:
    print("A válasz helyes")
else:
    print(f"A válasz helytelen, a helyes válasz a(z) {szam}")