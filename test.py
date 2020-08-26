print("Hallo Welt")
print()
variablenname ="https://www.python-lernen.de"
print(variablenname)
print()
kursname = "    Python Kurs"
vorname = "Philip"
print(kursname.lower())
print(kursname)
print("Der Kursname ist", len(kursname), "Zeichen lang")
print(vorname)
pfad = "C:\\niedlicherverzeichnisname"
print(pfad)

strasse = 'Ku\'damm'
print(strasse)

macbethtext = """Schön ist hässlich, hässlich schön.
Wir weichen wie Wolken und Windeswehn."""
print(macbethtext)


#lstrip(), rstrip() und strip() zum entfernen von zeichen () wenn nichts drinne ist leerzeichen
inhalt = "120      Berg                           "
ausgabe = inhalt.lstrip('1 20')
print(ausgabe)
print(ausgabe + ",der wandert")
inhalt2 = "  1.)          Testtext         "
ausgabe2 = inhalt2.strip('.)  1234567890')
print(ausgabe2)

#ljust() fügt füllt angegebene Stellen auf,
#ljust() = String wird linksbündig zurückgeliefert (Füllzeichen möglich)
#center() = String wird zentriert ausgegeben (Füllzeichen möglich)
#rjust() = String wird rechtsbündig zurückgeliefert (Füllzeichen möglich)
#zfill() = String wird mit Nullen (Zero) aufgefüllt
inhalt3 = "Vier"
ausgabe3 = inhalt3.ljust(2,'~')
print(ausgabe3, "mehr text")
print(inhalt3.center(20))
print(inhalt3.zfill(8))
#lower() = alles klein schreiben. upper() = alles gross schreiben
inhaltklein = "klein geschrieben"
grossgeschrieben = inhaltklein.upper()
print(grossgeschrieben)
sondertext = "Ich bin ein besonderer Text ühüöähößßßß"
print("Umwandlung durch casefold:")
print(sondertext.casefold())

#reversed(str), .join(), list() um ein eventuelles Palindrom zu erzeugen
ptext = "Rentner"
ptext = ptext.casefold()
rueckwarts = ''.join(reversed(ptext))
print(ptext)
print(rueckwarts)

if ptext == rueckwarts:
    print(ptext, "ist ein Palindrom")
else:
    pring("KEIN Palindrom")
print()
#capitalize() schreibe den ersten Buchstaben groß, alle anderen klein
#title() jeden Anfangsbuchstaben
#swapcase() dreht alles um
#replace('x','y')
#count() zählt ein Bestimmtes Vorkommen
vornachname  = "Rolf von und zu Maier-Müller"
umgewandelt  = vornachname.capitalize()
umgewandeltt = vornachname.title()
umgewandelts = vornachname.swapcase()
print(umgewandelt)
print(umgewandeltt)
print(umgewandelts)
print()
replacetext = "Der Preis für 2 Socken beträgt 5 DM und 5 Paar kosten 10 DM"
print(replacetext)
replacetext = replacetext.replace("DM", "Euro")
print("Nach den Austauschen über replace():")
print(replacetext)
print()
inhaltc = "Hier kommt ein String-Inhalt"
print(inhaltc.count("h",))
print()
#endswith() checkt ob die endung, hier in einem tupel definiert, stimmt
inhaltd = "https.//www.python-lernen.de"
datentyp_tupel =(".de", ".com", ".net")
ergebnis = inhaltd.endswith(datentyp_tupel)
print("endet der Link auf .de, .com oder .net?")
print(ergebnis)
#das gleiche gibt es auch mit .startswith() da wird der anfang geprüft
#.partition() teil den string an erster eingetragener stelle mit einem ","
#zusammenfügen per join()
deutschenglisch = {'null': 'zero', 'eins': 'one'}
trennzeichen = "#"
ergebnis = trennzeichen.join(deutschenglisch)
print(ergebnis)
print()
print(3 * 'mi')
#Computer fangen immer bei "0" an zu zählen, letztes listenelement wird mit -1 angesprochen
print()
#mit append() etwas ans ende einer liste anhängen
buchstaben = []
print(buchstaben)
buchstaben.append('a')
buchstaben.append('b')
print(buchstaben)
print()
#mit insert() kann man auswählen was und wo man etwas einfügen will, mit del löscht man ein Element
#pop() löscht den letzten Eintrag einer Liste, remove () entfernt angegebenen wert zbsp "b"
buchstaben = ['a', 'b']
print(buchstaben)
buchstaben.insert(1, 'c')
print(buchstaben)
print()
#datentyp dictionary
deutschenglisch = {}
deutschenglisch['null'] = 'zero'
deutschenglisch['eins'] = 'one'
deutschenglisch['zwei'] = 'two'
deutschenglisch['drei'] = 'three'
print(deutschenglisch)
print(deutschenglisch.keys())
print(deutschenglisch.items())
#Variablen speichern EINEN Inhalt, Listen VIELE, beides änderbar. Tupel speichern VIELE Inhalte
#UNVERÄNDERLICH
print()
#set gibt jeden wert einmal aus
werte_als_tupel = (1,1,1,3,5,3,4,5,3)
werte_als_set   = set(werte_als_tupel)
print(werte_als_set)
print()
#Das Besondere ist nun, dass über 2 Sets Mengenlehre mit „Schnittmenge“,
# „Vereinigungsmenge“, „A ohne B“ usw. durchgeführt werden kann.
set_a = { 1, 2, 3, 'A', 'B', 'C' }
set_b = { 2, 3, 'B', 'D' }
print( set_a & set_b )
print()
set_a = { 1, 2, 3, 'A', 'B', 'C' }
set_b = { 2, 3, 'B', 'D' }

print("Set A:")
print(set_a)

print("Set B:")
print(set_b)
print()

print("Schnittmenge über &")
print( set_a & set_b )
print()

print("Vereinigungsmenge über |")
print( set_a | set_b )
print()

print("Differenzmenge über - ")
print( set_a - set_b )
print()

print("Symmmetrische Differnz (entweder-oder) über ^")
print( set_a ^ set_b )
print()

print("Obermenge von  > ")
print( set_a > set_b )
print()
print()
inhalt = "Buchstaben zählen"
for einzelbuchstabe in sorted(list(set(inhalt))):
    print(einzelbuchstabe, ": Anzahl", inhalt.count(einzelbuchstabe))
print()
print()
#Eingabe mit input
benutzereingabe = input("Bitte Zahl eingeben")
benutzereingabe = int(benutzereingabe)
print(type(benutzereingabe))
print("Eingegeben wurde :" + str(benutzereingabe))
print()
#unsichtbare eingabe:
from getpass import getpass

nutzername = input("Nutzername: ")
kennwort   = getpass("Passwort: ")

print("Eingegebener Nutzername", nutzername)
print("Eingegebenes Kennwort", kennwort)
print()
#if Bedingung
wert = int(input("Zahl eingeben: ",))
if wert < 5:
    print('Wert ist kleiner als 5')
if wert == 5:
    print('Wert ist exakt 5')
elif wert == 6:
    print('Wert ist exakt 6')
#!!nicht elseif sonder elif!!
else:
    print('Wert ist größer als 5')
print('und hier geht es nach der if-Abfrage weiter')
