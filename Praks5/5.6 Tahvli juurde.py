from datetime import *

#variables
file = open("nimekiri.txt")
names = []
date = datetime.now().day

for row in file:
    names.append(row.strip())

print(names[date-1])