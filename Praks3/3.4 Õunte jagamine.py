from random import randint

mitupöialpoissi = int(input("sisestage täringute arv (0-7): "))
val = 0
õunad = 14

while val < mitupöialpoissi:
    rand = randint(1,2)
    õunad = õunad - rand
    print("Pöialpoiss sai " + str(rand) + " õuna.")
    val = val + 1
print("Lumivalgekesele jäi " + str(õunad) + " õuna.")