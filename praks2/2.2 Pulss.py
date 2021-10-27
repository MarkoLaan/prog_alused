vanus = int(input("sisestage vanus: "))
sugu = input("sisestage sugu: ")
trentüüp = int(input("sisestage treeningu tüüp1 - tervisetreening, 2 - põhivastupidavuse treening, 3 - intensiivne aeroobne treening: "))

if sugu == "M" or sugu == "m":
    pulsemax = 220 - vanus
elif sugu == "N" or sugu == "n":
    pulsemax = 206 - vanus * 0.88

if trentüüp == 1:
    minpulse = 0.5 * pulsemax
    maxpulse = 0.7 * pulsemax
elif trentüüp == 2:
    minpulse = 0.7 * pulsemax
    maxpulse = 0.8 * pulsemax
elif trentüüp == 3:
    minpulse = 0.8 * pulsemax
    maxpulse = 0.87 * pulsemax
    
maxpulse = round(maxpulse)
minpulse = round(minpulse)
print("Pulsisagedus peab olema vahemikus " + str(minpulse) + " ja " + str(maxpulse) + " vahel.")