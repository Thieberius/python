# eine von den 5 wählen!
from konto import *

# oder
from konto import Konto

# oder
from konto import Pluskonto

# oder
from konto import Konto, Pluskonto

# oder
import konto

kunde_schulz = Konto("000111555")
kunde_schulz.kontostand_anzeigen()
kunde_schulz.geld_einzahlen(400)
kunde_schulz.geld_abheben(150)
kunde_schulz.kontostand_anzeigen()

kunde_minderjaehrig = Pluskonto("0000935")
kunde_minderjaehrig.kontostand_anzeigen()
kunde_minderjaehrig.geld_einzahlen(200)
kunde_minderjaehrig.geld_abheben(101)
kunde_minderjaehrig.kontostand_anzeigen()
