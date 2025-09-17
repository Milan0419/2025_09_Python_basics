x = int(input("Hány fok van: "))

if x > 30:
    print("Forróság, igyál sok vizet!")
elif 21 <= x <= 30:
    print("Kellemes idő.")
elif 0 <= x < 21:
    print("Hűvös, kabát ajánlott.")
elif x < 0:
    print("Nagyon hideg, öltözz melegen!")
