def budget(visitrs):
    budget1 = visitrs * 10 + 55
    return (budget1)

inv = []


filename = input("Failinimi: ")

file = open(filename)

for row in file:
    inv.append(row)
print(len(inv))

kindlad_kulalised = 0
for inimene in inv:
    if  inimene[0] == '+':
        kindlad_kulalised += 1
        
print(kindlad_kulalised)

kutsutud = int(len(inv))
tuleb = int(kindlad_kulalised)

print("Maksimaalne eelarve on: " + str(budget(kutsutud)))
print("Minimaalne eelarve on: " + str(budget(tuleb)))