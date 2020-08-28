class Katze():
    """ Klasse für das Erstellen von Katzen
    Hilfetext ideal bei mehreren Programmieren in
    einem Projekt oder wenn man ein schlechtes
    Gedächtnis hat """

    def __init__(self, rufname, augenfarbe, gewicht, groesse, farbe="schwarz", alter=0):
        self.rufname    = rufname
        self.farbe      = farbe
        self.alter      = alter
        self.augenfarbe = augenfarbe
        self.gewicht    = gewicht
        self.groesse    = groesse
        self.schlafdauer= 0

    def tut_miauen(self, anzahl = 1):
        print(anzahl * "miau ")

    def tut_schlafen(self, dauer):
        print(self.rufname, "schläft jetzt", dauer , "Minuten ")
        self.schlafdauer += dauer
        print(self.rufname, "schläft insgesamt:", self.schlafdauer, "Minuten")

katze_sammy = Katze("Sammy", "orange", "blau", 3, "8Kg", "95cm")
katze_sammy.tut_miauen()
print(katze_sammy.rufname)
print(katze_sammy.farbe)
print(katze_sammy.augenfarbe)
print(katze_sammy.gewicht)
print(katze_sammy.groesse)
print(katze_sammy.alter)
katze_karlo = Katze("Karlchen", "grün", "30Kg", "normal")
katze_karlo.tut_schlafen(3)
katze_karlo.tut_miauen(3)
katze_karlo.tut_schlafen(20)
print("Name: "        , katze_karlo.rufname)
print("Fellfarbe: "   , katze_karlo.farbe)
print("Augenfarbe: "  , katze_karlo.augenfarbe)
print("Gewicht: "     , katze_karlo.gewicht)
print("Groesse: "     , katze_karlo.groesse)
print("Alter: "       , katze_karlo.alter)
