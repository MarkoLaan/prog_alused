#variables
file1 = open("sisseranne.txt")
file2 = open("valjaranne.txt")

vallist1 = []
vallist2 = []
 
#code..
for row in file1:
    vallist1.append(int(row.strip()))

for row in file2:
    vallist2.append(int(row.strip()))

print(vallist1)
print(vallist2)

difflist = []
for i in range(0, len(vallist1)):
    diff = vallist1[i] - vallist2[i]
    difflist.append(diff)
    
print(difflist)
maxdiff = max(difflist)

thisvalue = difflist.index(maxdiff)

if maxdiff >= 0:
    print("Suurim positiivne rändesaldo oli " + str(thisvalue+1) + ". aastal.")
else:
    print("Positiivse rändesaldoga aastaid pole")