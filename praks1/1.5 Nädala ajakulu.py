aine_punktid = int(input("Sisestage aine punktid :"))
nädalate_arv = int(input("Sisestage nädalate arv :"))
ajakulu = (aine_punktid * 26)
eeldatav_ajakulu = round(ajakulu / nädalate_arv)
print ("Teie eeldatav ajakulu on "
         + str(eeldatav_ajakulu))