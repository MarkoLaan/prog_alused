#variables
filename = input("Sisestage failinimi: ")
file = open(filename)
order = 0
songlist = []

#code..
for row in file:
    songlist.append(row)
    order = order + 1
    print(str(order) + ". " + row.strip())
    
file.close()
#print(songlist)
songselect = int(input("Sisestage laulu järjekorranumber: "))

print("Praegu mängib: " + songlist[songselect - 1])
