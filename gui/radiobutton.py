import tkinter as tk
root = tk.Tk()

def ausgabe():
    print(ausgewaehlt.get())
    aktuell_ausgewaehlt = ausgewaehlt.get()
    textausgabe = tk.Label(root, text=aktuell_ausgewaehlt, bg="orange")
    textausgabe.pack()

anrede = ["Frau", "Herr"]
ausgewaehlt = tk.StringVar()
for einzelwert in anrede:
    radiob = tk.Radiobutton(root, text=einzelwert, value=einzelwert, variable=ausgewaehlt).pack()

root.mainloop()
