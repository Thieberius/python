import tkinter as tk

fenster = tk.Tk()

def ausgabe():
    print(lbox.curselection())
    aktuell_ausgewaehlt = lbox.curselection()
    textausgabe = tk.Label(fenster, text=aktuell_ausgewaehlt, bg="orange")
    textausgabe.pack()

einkaufsliste = ["Mehl", "Butter", "Hefe", "Wasser", "O-Saft", "Haferflocken"]

lbox = tk.Listbox(fenster)
lbox.pack()

for lebensmittel in einkaufsliste:
    lbox.insert("end", lebensmittel)

schaltf1 = tk.Button(fenster, text="Aktion durchführen", command= ausgabe)
schaltf1.pack()

fenster.mainloop()
