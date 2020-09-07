import sqlite3
verbindung = sqlite3.connect("geburtstage.db")
zeiger = verbindung.cursor()
zeiger.execute("SELECT * FROM personen")
inhalt = zeiger.fetchall()
print(inhalt)
UPDATE personen SET vorname='Johann Christoph Friedrich' WHERE nachname='Schiller'
verbindung.close()
