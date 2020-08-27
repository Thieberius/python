import random
durchgang = 0
aktiv = True
zufallzahl = random.randint(1,20)


while aktiv:
    durchgang = durchgang + 1
    print(durchgang)
    benutzereingabe = int (input("Bitte Zahl eingeben: "))

    if benutzereingabe == zufallzahl:
        print("Zahl erraten")
        aktiv = False
        break
    elif benutzereingabe > zufallzahl:
        print("deine Zahl ist zu groß")
    else:
        print("deine Zahl ist zu klein")
    if (durchgang == 5):
        print("Du hast leider verloren")
        print("Es war " + str(zufallzahl))
        aktiv = False
print("Ende des Spiels")
