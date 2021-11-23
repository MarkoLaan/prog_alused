def eelarve(külarv):
    eelarve1 = külarv * 10 + 55
    return (eelarve1)

kutsutud = int(input("Palju on kutsutud külalisi: "))
tuleb = int(input("Palju külalisi tuleb: "))

print("Maksimaalne eelarve on: " + str(eelarve(kutsutud)))
print("Minimaalne eelarve on: " + str(eelarve(tuleb)))