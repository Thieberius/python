class Tier():
    """ Klasse für das Erstellen von Säugetieren """

    def __init__(self, rufname, farbe, alter):
        self.rufname = rufname
        self.farbe   = farbe
        self.alter   = alter
        self.schlafdauer = 0
    def tut_schlafen(self, dauer):
        print(self.rufname, "schläft jetzt", dauer ,"Minuten")
        self.schlafdauer += dauer
        print(self.rufname, "schläft:", self.schlafdauer, "Minuten")
    def tut_reden(self, anzahl = 1):
        print(self.rufname, "sagt", anzahl * "miau ")

class Katze(Tier):


    def __init__(self, rufname, farbe, alter):

        super().__init__(rufname, farbe, alter)



class Hund(Tier):
    def __init__(self, rufname, farbe, alter):
        super().__init__(rufname, farbe, alter)

katze_sammy = Katze("Sammy", "orange", 3)
print(katze_sammy.rufname)
print(katze_sammy.farbe)
print(katze_sammy.alter)
katze_sammy.tut_reden(2)
print()
hund_bello = Hund("Bello", "braun", 5)
print(hund_bello.rufname)
print(hund_bello.farbe)
print(hund_bello.alter)
hund_bello.tut_schlafen(8)
