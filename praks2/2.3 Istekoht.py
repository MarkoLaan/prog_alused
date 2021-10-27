from random import randint

koht = ()
valik = input("Kas soovite istekoha valida ise või loosi teel? (ise/loos) : ")
if valik == "ise":
    istekoht = input("Aknakoht või mitte (aken/muu) : ")
elif valik == "loos":
    koht = randint(1, 3)
if koht == 1:
    print ("Istekoht loositi. Aknakoht")
elif koht == 2 or koht == 3:
    print ("Istekoht loositi. Vahekäigukoht")
    
elif istekoht == "aken":
    print ("Valisite ise. Aknakoht")
elif istekoht == "muu":
    print ("Valisite ise. Vahekäigukoht")