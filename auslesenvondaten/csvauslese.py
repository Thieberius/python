import csv

with open("adressen.csv") as csvdatei:
    csv_reader_object = csv.reader(csvdatei)

    zeilennummer = 0
    for row in csv_reader_object:

        if zeilennummer == 0:
            print(f'Spaltennamen sind: {", ".join(row)}')
        else:
            print(f'- Nachname: {row[0]} \t| Vorname: {row[1]} \t| Geburtstag: {row[2]}.')
        zeilennummer += 1

    print(f'Anzahl Datensätze: {zeilennummer-1}')
