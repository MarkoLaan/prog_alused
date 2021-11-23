def mahlapakkide_arv(õuntekogus):
    mahlapakkidearv = (õuntekogus) * 0.4 / 3
    return round(mahlapakkidearv)

õuntekogus = float(input("Õuntekogus (kg): "))
print(mahlapakkide_arv(õuntekogus))