class Jogger(list):
    """sportliche klasse für das verwalten von gelaufenen zeiten"""

    def __init__(self, altersklasse, zeit=[]):
        self.altersklasse = altersklasse
        self.gelaufene_zeiten = zeit

    def zeiterfassung(self, zeiten):
        self.gelaufene_zeiten += zeiten

laufer_Hans = Jogger("M40")
print(laufer_Hans.altersklasse)
laufer_Hans.zeiterfassung(["2:30"])
print(laufer_Hans.gelaufene_zeiten)
laufer_Hans.zeiterfassung(["2:40", "3:10"])
print(laufer_Hans.gelaufene_zeiten)

print()
print("vor POP:")
print(laufer_Hans.gelaufene_zeiten)
print("POP:")
print(laufer_Hans.gelaufene_zeiten.pop())
print("nach POP:")
print(laufer_Hans.gelaufene_zeiten)
