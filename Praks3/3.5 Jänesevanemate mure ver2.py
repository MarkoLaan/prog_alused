ringid = int(input("sisestage ringide arv: "))
crts = 0
val = 1

while val <= ringid:
    crts = crts + val
    val = val + 1
print (crts)