import tkinter as tk

def aktionSF():
    label3 = tk.Label(root, text="Aktion durchgeführt", bg="yellow")
    label3.pack()
def grad_nach_kelvin():
    #print(eingabefeld_wert)
    grad = int(eingabefeld_wert.get())
    kelvin = grad + 273
    textausgabe = tk.Label(root, text=kelvin, bg="lightblue").pack()

root = tk.Tk()
# Textausgabe erzeugen
label1 = tk.Label(root, text="Etwas umrechnen").pack()
schaltf1 = tk.Button(root, text="Grad in Kelvin", command=grad_nach_kelvin, highlightbackground="gold").pack()

schaltf2 = tk.Button(root, text="Aktion durchführen", command=aktionSF, cursor='hand2').pack(side="bottom")
#Grad - Fahrenheit umrechnen
eingabefeld_wert=tk.StringVar()
eingabefeld=tk.Entry(root, textvariable=eingabefeld_wert).pack()

root.mainloop()
