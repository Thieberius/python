import random
print()
print("mit sample")
print()
lottozahlen_alle = []
lottozahlen_alle.extend(range(1,50))
lottozahlen_gewinner = random.sample(lottozahlen_alle,6)
lottozahlen_gewinner.sort()
print(lottozahlen_gewinner)
print(random.choices(lottozahlen_gewinner, k=6))
print()
print("mit shuffle")
print()
import random
lottozahlen = []
lottozahlen.extend(range(1,50))
random.shuffle(lottozahlen)
for x in range(6):
	print(lottozahlen[x])
