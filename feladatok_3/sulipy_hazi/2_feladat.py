#Készíts egy programot, ami bekér egy számot a felhasználótól, majd kiírja, hogy a megadott szám páros-e vagy páratlan!


x = int(input("Írj be egy számot és megmondom hogy páros vagy páratlan: "))

if x % 2 == 0:
    print("Páros")
else: 
    print("Páratlan")