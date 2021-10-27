size = float(input("Kirja suurus: "))
topic = input("Kirja teema pealkiri: ")
file = input("Kas kiri on failiga(jah/ei): ")

if size < 1.0:
    if topic == "":
        print("Kiri on spämm")
    else:
        print("Kiri ei ole spämm")
else:
    print("Kiri ei ole spämm")
