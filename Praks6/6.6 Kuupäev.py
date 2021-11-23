def kuu_nimi(kuunum):
    kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    return kuud[kuunum-1]

def kuupäev_sõnena(kuupäev):
    kuupäev_järjend = kuupäev.split(".")
    print(kuupäev_järjend[0] + ". " +  kuu_nimi(int(kuupäev_järjend[1]))+ " " +  kuupäev_järjend[2] + ". a.")

sisestatud = input("Sisesta kuupäev kujul DD.MM.YYYY: ")

kuupäev_sõnena(sisestatud)