class Katze():
    """ Klasse für das Erstellen von Katzen
    Hilfetext ideal bei mehreren Programmieren in
    einem Projekt oder wenn man ein schlechtes
    Gedächtnis hat """

    def __init__(self, rufname, farbe, augenfarbe, alter, gewicht, groesse):
        self.rufname    = rufname
        self.farbe      = farbe
        self.alter      = alter
        self.augenfarbe = augenfarbe
        self.gewicht    = gewicht
        self.groesse    = groesse

katze_sammy = Katze("Sammy", "orange", "blau", 3, "8Kg", "95cm")
print(katze_sammy.alter)
print(katze_sammy.farbe)
print(katze_sammy.augenfarbe)
print(katze_sammy.gewicht)
print(katze_sammy.groesse)
print(katze_sammy.rufname)
