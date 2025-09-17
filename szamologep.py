def osszead(x, y):
    return x + y

def kivon(x, y):
    return x - y

def szoroz(x, y):
    return x * y

def oszt(x, y):
    return x / y

print("Válaszd ki mitakarsz csináni -\n"
      "1. Összeadni\n"
      "2. Kivonni\n"
      "3. Szorozni\n"
      "4. Osztani\n")

sel = int(input("Melyik te csöves (1-4): "))

num1 = int(input("Írd be az első számot: "))
num2 = int(input("Írd be a második számot: "))



if sel == 1:
    print(num1, "+", num2, "=", osszead(num1, num2))
elif sel == 2:
    print(num1, "-", num2, "=", kivon(num1, num2))
elif sel == 3:
    print(num1, "*", num2, "=", szoroz(num1, num2))
elif sel == 4:
    print(num1, "/", num2, "=", oszt(num1, num2))
else:
    print("Nemjo te csöves")