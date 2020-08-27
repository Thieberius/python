import datetime
import time
from datetime import date
aktuellesDatum = date.today()
print(aktuellesDatum)
weihnachten2020 = date(2020, 12, 24)
print(weihnachten2020.strftime("%d.%m.%Y"))
print()
weihnachten2020 = datetime.datetime(2020, 12, 4, 15, 30)
print(weihnachten2020.strftime("%H:%M:%S %d.%m.%Y"))
print()
aktuellesDatum = date.today()
wochentag_nr = aktuellesDatum.isoweekday()
#print(wochentag_nr)
wochentage_kuerzel = ["So", "Mo", "Di", "Mi", "Do", "Fr", "Sa"]
print("aktueller Wochentag: ", wochentage_kuerzel[wochentag_nr])
#
print()
#
print("Aktuelle Zeit und Datum:")
aktuelleZeit = time.asctime()
print(aktuelleZeit)
