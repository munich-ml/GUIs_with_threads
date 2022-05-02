import tkinter as tk

window = tk.Tk()

label = tk.Label(text="label")
entry = tk.Entry()
textbox = tk.Text()

label.pack()
entry.pack()
textbox.pack()

window.mainloop()