inimestearv = int(input("sisestage inimeste arv:"))
bussikohtatearv = int(input("sisestage bussi kohtate arv:"))
bussid = inimestearv // bussikohtatearv
mahajäänud = inimestearv % bussikohtatearv
print (mahajäänud)
if mahajäänud > 0:
    bussid + 1
print("Tuleb tellida " + str(bussid) + " bussi.")