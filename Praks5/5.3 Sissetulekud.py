#variables
file = open("konto.txt")
income = []

#..
for row in file:
    if float(row) > 0:
        income.append(row[:-1])

file.close()

print(income)

for element in income:
    print(element)