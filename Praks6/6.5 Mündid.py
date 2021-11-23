def pronksikarva_summa(järjend):
    summa = 0
    for element in järjend:
        if element == 1 or element == 2 or element == 5:
            summa = summa + element
    return summa

failinimi = input("sisestage faili nimi:")

fail = open(failinimi)
mündid = []
for row in fail:
    mündid.append(int(row))

fail.close()

summa = pronksikarva_summa(mündid)
print("Hoiupõrsasse läheb " + str(summa) + " senti.")