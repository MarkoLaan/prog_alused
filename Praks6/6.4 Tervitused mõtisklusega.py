def tervitus(arv):
    print("Võõrustaja: \"Tere!\"")
    print("Täna " + str(arv) + ". kord tervitada, mõtiskleb võõrustaja.")
    print("Külaline: \"Tere, suur tänu kutse eest!\"")
  
külalistearv = int(input("Külaliste arv: "))
  
kord = 1
while kord <= külalistearv:
    tervitus(kord)
    kord = kord + 1