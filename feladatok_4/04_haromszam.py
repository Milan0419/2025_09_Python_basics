print("Adj meg három számot és megmondom melyik a legnagyobb: ")
elso = int(input("Első szám: "))
masodik = int(input("Második szám: "))
harmadik = int(input("Harmadik szám: "))

if elso > masodik and elso > harmadik:
    print(f"A legnagyobb szám {elso}")
elif masodik > elso and masodik > harmadik:
    print(f"A legnagyobb szám {masodik}")
elif harmadik > elso and harmadik > masodik:
    print(f"A legnagyobb szám {harmadik}")