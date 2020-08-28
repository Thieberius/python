datei = open('text.txt','r')
print(datei.read())

datei = open('text.txt', 'w')
datei.write('\r\nweitere Zeile')

datei = open('text.txt', 'wb')



datei.close()
