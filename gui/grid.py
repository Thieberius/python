import tkinter as tk

root = tk.Tk()

label1 = tk.Label(root, text="Hallo Welt", bg="orange")
label1.grid(row=0, column=0)

label2 = tk.Label(root, text="R1 / C1", bg="lightgreen")
label2.grid(row=1, column=1)

label3 = tk.Label(root, text="R2 / C2", bg="lightblue")
label3.grid(row=2, column=2)

label4 = tk.Label(root, text="R2/C0", bg="yellow")
label4.grid(row=2, column=0, sticky='e')

root.mainloop()
