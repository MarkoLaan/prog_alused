from random import randint

dice = int(input("sisestage täringute arv: "))
val = 0

while val < dice:
    rand = randint(1,6)
    print(rand)
    val = val + 1