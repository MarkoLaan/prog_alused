nimi = input("Sisestage nimi:")
lubatud_kiirus = int(input("Sisestage lubatud kiirus km/h:"))
tegelik_kiirus = int(input("Sisestage tegelik kiirus km/h:"))
arvutus = (tegelik_kiirus - lubatud_kiirus) * 3
trahv = min(190, arvutus)
print (nimi + " kiiruse ületamise eest on teie trahv "
       + str(trahv) + " eurot.")