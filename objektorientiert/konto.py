""" Klasse Konto und Pluskonto zum verwalten, ein- und auszahlen von Bankkonten """

class Konto:
    """ unsere kleines Bankprogramm zum Verwalten Konten/Geld """
    __geldbestand = 0

    def __init__(self, kontonummer, kontostand=0):
        self.__kontonummer = kontonummer
        self.__kontostand  = kontostand

    def geld_abheben(self, betrag):
        print("Geld wird abgehoben:", betrag)
        self.__kontostand -= betrag
        Konto.__geldbestand -= betrag

    def geld_einzahlen(self, betrag):
        print("Geld wird eingezahlt:", betrag)
        self.__kontostand += betrag
        Konto.__geldbestand += betrag

    def kontostand_anzeigen(self):
        print("aktueller Kontostand: ", self.__kontostand)
        print("aktueller Geldbestand der Bank: ", Konto.__geldbestand, "\n")

    def kontostand_aktuell(self):
        return self.__kontostand

class Pluskonto(Konto):
    """ ein Konto, dass nicht überzogen werden kann """

    def __init__(self, kontonummer, kontostand=0):
        """ Initalisieren über Eltern-Klasse """
        super().__init__(kontonummer, kontostand=0)

    def geld_abheben(self, betrag):
        print("Geld soll vom Pluskonto abgehoben werden:", betrag)
        print("Maximal verfügbar ist gerade:", self.kontostand_aktuell())

        if self.kontostand_aktuell() - betrag >= 0:
            print("Auszahlen von Pluskonto: ", betrag)
            super().geld_abheben(betrag)
        else:
            print("Sorry, Konto kann nicht überzogen werden!")
