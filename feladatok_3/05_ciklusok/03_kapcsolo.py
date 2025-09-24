folytatja = True
while folytatja:
    print("VIDD KI A SZEMETET")
    valasz = input("Elmondjam megegyszer? (i/n) ")
    if valasz ==  'n' or valasz == 'nem' or valasz == 'no':
        folytatja = False
    elif valasz == 'i' or valasz == 'igen' or valasz == 'yes':
        folytatja =  True
    else:
        print("A válasz helytelen")
        folytatja = False
print(">> Program vége! <<")