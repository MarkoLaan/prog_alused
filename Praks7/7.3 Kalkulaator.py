from easygui import *

options = ["+", "-", "*"]

val1 = integerbox("Sisestage täisarv vahemikus 1-10", lowerbound = 1, upperbound = 10)

val2 = integerbox("Sisestage teinetäis arv vahemikus 1-10", lowerbound = 1, upperbound = 10)

optionselect = buttonbox("Valige tehe", choices = options)

if optionselect == "+":
    awnser = val1 + val2
    
elif optionselect == "-":
    awnser = val1 - val2
    
elif optionselect == "*":
    awnser = val1 * val2

msgbox("vastus on " + str(awnser))
