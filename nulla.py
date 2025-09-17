'''
szam = int(input("Írj be egy számot és megmondom hogy negatív vagy nem: "))
if szam < 0:
    print("A szám negatív")
else:
    print("A szám nem negatív")
'''

szam = int(input("Adj meg egy ilyen szamféleséget: "))

if szam == 0:
    print("Nulaaaa")
elif szam % 2 == 0: 
    print("Páros")
else:
    print("Páratlan")