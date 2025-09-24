"""A csoport:
Készítsünk programot, amely labdák csomagolásához végez számításokat.
A labdákat szalaggal kell átkötni úgy, hogy kétszer körbe érje őket, és a masni készítéséhez számolunk még 60 cm-t.
A labda körül a szalag egy kör (kerület képlete 2*r*PI)
A program kérje be a labda átmérőjét, a labdák számát, és a rendelkezésre álló szalag hosszát!
Számítsa ki, és írja a képernyőre, hogy a bekért számú labda csomagolásához hány centiméter szalagra van szükség, valamint állapítsa meg,
hogy elegendő szalagunk van-e a művelet elvégzéséhez, és ezt is közölje a felhasználóval!
"""

print("Labda szalaggal való átkötésének kiszámítása")

atmero = float(input("Mekkora a labda átmérője?"))
labdakszama = float(input("Mennyi labda van?"))
szalaghossz = float(input("Mennyi szalag van?"))

PI =  3.14
szamolas = 2 * atmero * labdakszama * PI
szukseges = 2 * szamolas + 60


if szalaghossz < szukseges:
    print(f"Nincs elegendő szalag! Szükséges szalag: {szukseges}")
elif szalaghossz > szukseges:
    print(f"Szükséges szalag: {szukseges}")
    print("Van elegendő szalag!")
else:
    print("Error 404")
    