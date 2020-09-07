import sqlite3
verbindung = sqlite3.connect("geburtstage.db")
zeiger = verbindung.cursor()
zeiger.execute("SELECT nachname, geburtstag, vorname FROM personen")
inhalt = zeiger.fetchall()
print(inhalt)
verbindung.close()
