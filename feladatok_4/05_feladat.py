ev = int(input("Írj be egy évszámot: "))

if ev % 400 == 0 and ev % 100 == 0 or ev % 4 ==0 and ev % 100 != 0:
    print("{0} szökőév".format(ev))  
else:
    print("{0} nem szökőév".format(ev))