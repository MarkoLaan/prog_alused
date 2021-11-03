ringid = int(input("sisestage ringide arv: "))
crts = 0
val = 1

while val <= ringid:
    if val % 2 == 0:
        crts = crts + val
    val = val + 1
print (crts)