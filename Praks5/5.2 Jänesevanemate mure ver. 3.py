#variables
lapnum = int(input("Ringide arv: "))
#crts = 0
crts = []

#..
for num in range(1, lapnum+1, 1):
    if num % 2 == 0:
        #crts = crts + num
        crts.append(num)
    
print(sum(crts))