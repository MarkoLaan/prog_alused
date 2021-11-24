filename = input("Sisestage faili nimi: ")

file = open(filename, encoding="UTF-8")


text = file.read()
print(text.upper().replace("Ä","AE").replace("Ö","OE").replace("Õ","OE").replace("Ü","UE"))