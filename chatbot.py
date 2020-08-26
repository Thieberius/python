# -*- coding: utf-8 -*-
import random
zufallsantworten = ["Oh, wirklich", "Interessant ...", "Das kann man so sehen", "Ich verstehe ..."]
reaktionsantworten = {"hallo": "Moin Moin Seeman!",
                      "geht": "Ziehmlich raue See heute!",
                      "essen": "Matjesfilet natürlich"
                    }
print("Moin Moin")
print("Worüber wollen wir schnacken?")
print("Wenn du keine Lust mehr hast, einfach 'bye' eingeben.")
print("")
nutzereingabe = ""
while nutzereingabe != "bye":
    nutzereingabe = ""
    while nutzereingabe == "":
        nutzereingabe = input("Dein Seemansgarn: ")
    nutzereingabe = nutzereingabe.lower()
    nutzerwoerter = nutzereingabe.split()
#   print(nutzerwoerter)
    intelligenteAntworten = False
    for einzelwoerter in nutzerwoerter:
        if einzelwoerter in reaktionsantworten:
            print(reaktionsantworten[einzelwoerter])
            intelligenteAntworten = True
    if intelligenteAntworten == False:
        print(random.choice(zufallsantworten))
        print(random.choice(zufallsantworten))
print("Ruhige See!")
exit()
