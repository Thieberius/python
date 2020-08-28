import nltk

inhalt = """Der Erlkönig
Wer reitet so spät durch Nacht und Wind?
Es ist der Vater mit seinem Kind;
Er hat den Knaben wohl in dem Arm,
er faßt ihn sicher, er hält ihn warm.
Mein Sohn, was birgst du so bang dein Gesicht?
Siehst, Vater, du den Erlkönig nicht?
Den Erlkönig mit Kron und Schweif? -
Mein Sohn, es ist ein Nebelstreif. -
"Du liebes Kind, komm geh mit mir!
"""
satzzeichen = (",", ";", ":", ".", "?", "!", "''", '""', "-", "_")
for unerwuenschtes in satzzeichen:
    inhalt = inhalt.replace(unerwuenschtes, "")

woerter = inhalt.split()
worthaeufigkeit = nltk.FreqDist(woerter)
print(worthaeufigkeit)
print(worthaeufigkeit.most_common())
print(worthaeufigkeit.plot(20))
