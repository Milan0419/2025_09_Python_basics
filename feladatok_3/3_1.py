"""
1. Feladat
Thonny fejlesztői környezetben készíts egy rövid programot, amely
kommentként tartalmazza a program funkciójának leírását,
konstansként tárolja PI értékét,
egy másik változóban tárolja egy kör sugarának nagyságát (cm-ben megadva),
kiszámolja és a képernyőre kiírja a kör kerületét és területét!
[Megjegyzés] A szorzás jele: *
"""


radius = float(input("Kör sugara: "))
pi = 3.14
ker = 2 * radius * pi
ter = pi * radius * radius
print(f"""A kör kerülete: {ker} cm
      A kör területe: {ter} cm2""")