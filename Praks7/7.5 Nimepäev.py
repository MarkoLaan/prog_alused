from urllib.request import urlopen
#inputs

month = input("Kuunimi: ")
day = int(input("Kuupäev: "))

web = urlopen("http://kodu.ut.ee/~eno/mooc/"+month)

#code?

raw = web.read()
text = raw.decode()
lines = text.splitlines()

web.close

print("Kuupäeval " + str(day) + ". " + str(month) + " on nimepäevad inimestel nimega." + '\n' + lines[day+1])