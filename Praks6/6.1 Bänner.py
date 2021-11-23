def banner(lause):
    return lause.upper()

korda = int(input("Mittu korda korrata: "))
kasutaja_lause = input("Sisestage reklaam lause: ")
kord = 1
while kord <= korda:
    print(banner(kasutaja_lause))
    kord = kord + 1