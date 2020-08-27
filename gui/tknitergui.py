import tkinter as tk
root = tk.Tk()
#textausgabe erzeugen
label1 = tk.Label(root, text = "Ahoj Seemann", fg="black", bg="crimson")
#
#in gui elemente einbetten
label1.pack()
#
#grafik einbetten
bild1 = tk.PhotoImage(file="biene.png")
label2 = tk.Label(root, image=bild1).pack(side="left")




root.mainloop()
