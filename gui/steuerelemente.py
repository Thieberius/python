import tkinter as tk

root = tk.Tk()

gruppehobby = tk.LabelFrame(root, text="Ihre Hobbies?")
gruppehobby.pack()

checkbox01 = tk.Checkbutton(gruppehobby)
checkbox01["text"] = "Sport treiben"
checkbox01.pack(anchor="w")
checkbox01var = tk.BooleanVar()
checkbox01["variable"] = checkbox01var

checkbox02 = tk.Checkbutton(gruppehobby)
checkbox02["text"] = "Lesen"
checkbox02.pack(anchor="w")
checkbox02var = tk.BooleanVar()
checkbox02["variable"] = checkbox02var

checkbox03 = tk.Checkbutton(gruppehobby)
checkbox03["text"] = "Filme schauen"
checkbox03.pack(anchor="w")
checkbox03var = tk.BooleanVar()
checkbox03["variable"] = checkbox03var

root.mainloop()
