def bspfunktionfuerrueckgabe(eingabewert):
	rueckgabewert = eingabewert * 2
	return rueckgabewert
ergebnisausfunktion = bspfunktionfuerrueckgabe (5)
print(ergebnisausfunktion)
print()
#
#lokale variablen
#
variablenWert1 = "außerhalb der Funktion"
print("Variablenwert vor Funktion:", variablenWert1)
def bspfunktion():
	variablenWert1 = "IN der Funktion"
	print("Variablenwert in Funktion:", variablenWert1)
bspfunktion()
print("Variablenwert nach Funktion:", variablenWert1)
print()
#
#globale variablen
#
variablenWert = "außerhalb der Funktion"
print("Variablenwert vor Funktion:", variablenWert)
def bspfunktion():
    global variablenWert
    variablenWert = "IN der Funktion"
    print("Variablenwert in Funktion:", variablenWert)
bspfunktion()
print("Variablenwert nach Funktion:", variablenWert)
print()
#
#nonlocale variablen
#
variable = "Inhalt außerhalb gesetzt"
def grundfunktion():
	variable = "Inhalt innerhalb gesetzt"
	def fkt_local():
		variable = "Inhalt innerhalb local"
	def fkt_nonlocal():
		nonlocal variable
		variable = "Inhalt innerhalb nonlocal"
	def fkt_global():
		global varibale
		variable = "Inhalt innerhalb global"
	print("2. in Fkt: ", variable)
	fkt_local()
	print("3. in Fkt – flt_local aufgerufen: ", variable)
	fkt_nonlocal()
	print("4. in Fkt – flt_nonlocal aufgerufen: ", variable)
	fkt_global()
	print("5. in Fkt – flt_global aufgerufen: ", variable)
print("1. vor Funktionsaufruf: ", variable)
grundfunktion()
print("6. nach Funktionsaufruf: ", variable)
