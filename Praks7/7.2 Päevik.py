from datetime import datetime
date_time = datetime.today()
thisonestring = str(date_time)

filename = input("Sisestage failinimi: ")

writeinput = input("Sisestage oma sissekanne: ")

file = open(filename, "a", encoding="UTF-8")

file.write(thisonestring + "\n")
file.write(writeinput + "\n")

file.close()