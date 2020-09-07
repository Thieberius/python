class Tier():
    """ Klasse für das Erstellen von Säugetieren """
    tieranzahl = 0

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
    def anzahl_tiere():
        print("aktuelle Anzahl: ", Tier.tieranzahl)

class Katze(Tier):

    def __init__(self, rufname, farbe, alter):
        super().__init__(rufname, farbe, alter)
        Tier.tieranzahl += 1


class Hund(Tier):


    def __init__(self, rufname, farbe, alter):
        super().__init__(rufname, farbe, alter)
    def tut_reden(self, anzahl = 1):
        print(self.rufname, "sagt: ", anzahl * "whau ")
        Tier.tieranzahl += 1

katze_sammy = Katze("Sammy", "orange", 3)
print(katze_sammy.rufname)
print(katze_sammy.farbe)
print(katze_sammy.alter)
katze_sammy.tut_reden(2)
Tier.anzahl_tiere()
print()

katze_hope = Katze("Hope", "braun", 4)
print(katze_hope.rufname)
Tier.anzahl_tiere()

hund_bello = Hund("Bello", "braun", 5)
print(hund_bello.rufname)
print(hund_bello.farbe)
print(hund_bello.alter)
Tier.anzahl_tiere()

hund_bello.tut_schlafen(8)
hund_bello.tut_reden(4)
