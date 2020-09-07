import tkinter as tk
import sqlite3
fenster = tk.Tk()
label1 = tk.Label(fenster)


def ausgabe():
    print(lbox.curselection())
    aktuell_ausgewaehlt = lbox.curselection()
    dbausgabe = tk.Label(fenster, text=aktuell_ausgewaehlt, bg="orange").pack()


def erlkng():




text1 = tk.Label(fenster, text = "Datenbank", fg = "black").pack()
fenster.mainloop()
