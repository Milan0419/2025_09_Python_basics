szam = int(input("Adj meg egy ilyen szamféleséget: "))

if szam == 0:
    print("Nulaaaa")
elif szam % 2 == 0: 
    print("Páros")
else:
    print("Páratlan")