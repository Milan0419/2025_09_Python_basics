import random

x =  random.randint(1, 2)

coin = int(input("Fej(1) vagy írás(2): "))

print(f"A coin {x}")

if coin == x:
    print(f"Eltaláltad!")
    
else:
    print("Vesztettél!")