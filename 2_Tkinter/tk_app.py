import tkinter as tk
from tkinter import tix
import sys

PADX, PADY = 5, 3      # Widget padding

window = tk.Tk()
upper_frame = tk.Frame()
lower_frame = tk.Frame()
for frame in (upper_frame, lower_frame):
    frame.pack(padx=PADX, pady=PADY, fill=tk.X)

labels = ("input", "fibunacci(input)", "compute time [s]")
for row, text in enumerate(labels):
    label = tk.Label(upper_frame, text=text)
    label.grid(row=row, column=0, padx=PADX, pady=PADY, sticky="w")

input_ = tk.Spinbox(upper_frame, width=10, from_= 10, to=50)
entry_fib = tk.Entry(upper_frame)
entry_time = tk.Entry(upper_frame)
for row, widget in enumerate((input_, entry_fib, entry_time)):
    widget.grid(row=row, column=1, padx=PADX, pady=PADY, sticky="w")


def on_button_main():
    print("button main thread clicked")
    
button_main = tk.Button(lower_frame, text="compute in main thread", command=on_button_main)
button_worker = tk.Button(lower_frame, text="compute in worker thread", command=on_button_main)
for column, button in enumerate((button_main, button_worker)):
    button.grid(row=0, column=column, padx=PADX, pady=PADY)


window.mainloop()
