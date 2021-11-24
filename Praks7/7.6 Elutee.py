#argument s on sõne, esialgu see on kuupäev, edasi juba arvutatud arv
def elutee(s):
    #abimuutaja numbri arvutamiseks
    n = 0
    # tsükkel, mis vaatab iga sümboli sõnes
    for i in s:
        if i != ".":
            n += int(i) # arvutame summat
    # kui saadud arv on väiksem kui 10, siis ongi elutee number käes
    if n < 10:
        return n
    # kui saadud arv on 10 või suurem, siis on vaja uuesti arvutada,
    #selleks kasutame jälle sama funktsiooni
    else:
        return elutee(str(n))
    
#elutee('07.02.1969'))
 
openfile = open("sunnikuupaevad.txt", )

for row in openfile:
    eluteenumber = elutee(row.strip())
    failinimi = "elutee" + str(eluteenumber) + ".txt"
    f = open(failinimi, "a", encoding="UTF-8")
    f.write(row)
    f.close()


