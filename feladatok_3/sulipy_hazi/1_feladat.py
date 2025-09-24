#Készíts egy programot, amely megkérdezi a felhasználótól, hogy jó napja van-e! A válasz kétféle lehet: igen vagy nem. A választól függően írjon ki üzenetet a gép!

x = input("Jó napod van? Igen/Nem: ")

if x.lower() in ["igen", "i"]:
    print("Legyen továbbra is szép napod!")
elif x.lower() in ["nem", "n"]:
    print ("Remélem jobban fogod érezni magad!")
else: 
    print("Sajnos nem értettem a válaszod!")