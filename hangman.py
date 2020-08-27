#"Fehlversuche" werden bei jeder eingabe abgezogen, so ist mit
#7 fehlversuchen nur ein wort mit maximal 7 buchstaben zu erraten
import random
print("hangman in python")
print()
woerter = 'Xylophon Computer'.split()
erraten = []
nutzereingabe = ""
fehlversuche = 7
ratewort = random.choice(woerter)
#erst wird alles festgelegt was in den unteren bedingungen benutzt wird
for buchstaben in ratewort:
    erraten.append('_')
while nutzereingabe != "bye":
    for ausgabe in erraten:
        print(ausgabe, end=' ')
    print()
    nutzereingabe = input("Ihr Vorschlag: ")
    x=0
    for buchstaben in ratewort:
        if buchstaben.lower() == nutzereingabe.lower():
            print ("Treffer")
            erraten[x] = buchstaben
        x += 1
    # Kontrolle ob gewonnen
    if '_' in erraten:
        fehlversuche -= 1
        if fehlversuche == 0:
            print('Schade....verloren!')
            break
    else:
        print('gewonnen, das Wort war: ', ratewort)
        break
