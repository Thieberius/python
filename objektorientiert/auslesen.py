datei = open('geburtstage.db','r')
print(datei.read())

datei = open('geburtstage.db', 'w')
datei.write('\r\nweitere Zeile')

datei = open('geburtstage.db', 'wb')



datei.close()
