#variables
file = open("rebased.txt", encoding="UTF-8")
year = int(input("Sisestage aasta vahemikus 2011-2019: "))
val = 0
accepted = []

#..
for row in file:
    accepted.append(int(row))
    
file.close()

print(accepted[year-2011])