def bspfunktionfuerrueckgabe(eingabewert):
	rueckgabewert = eingabewert * 2
	return rueckgabewert
def hallomeister():
	print("Hallo Herr und Meister")
if __name__ == "__main__":
	print("Datei wurde direkt aufgerufen und die Main wird ausgeführt")
else:
	print("Datei wurde als Modul aufgerufen")

print("Ich stehe in der Datei: " + __name__)
