import tkinter as tk
from collections import OrderedDict

PADX, PADY = 5, 3      # Widget padding


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Tkinter threading demonstrator')
        
        self.frames = OrderedDict()
        for name in ("upper", "lower"):
            self.frames[name] = tk.Frame()
            self.frames[name].pack(padx=PADX, pady=PADY, fill=tk.X)

        self.labels = OrderedDict()
        for row, name in enumerate(("input", "fibunacci(input)", "compute time [s]")):
            self.labels[name] = tk.Label(self.frames["upper"], text=name)
            self.labels[name].grid(row=row, column=0, padx=PADX, pady=PADY, sticky="w")

        self.widgets = OrderedDict()
        self.widgets["input"] = tk.Spinbox(self.frames["upper"], width=10, from_= 10, to=50)
        self.widgets["fibunacci"] = tk.Entry(self.frames["upper"])
        self.widgets["time"] = tk.Entry(self.frames["upper"])
        for row, widget in enumerate(self.widgets.values()):
            widget.grid(row=row, column=1, padx=PADX, pady=PADY, sticky="w")

        self.buttons = OrderedDict()
        self.buttons["main"] = tk.Button(self.frames["lower"], text="compute in main thread", command=self.on_button_main)
        self.buttons["worker"] = tk.Button(self.frames["lower"], text="compute in worker thread", command=self.on_button_main)
        for column, button in enumerate(self.buttons.values()):
            button.grid(row=0, column=column, padx=PADX, pady=PADY)
            
            
    def on_button_main(self):
        for name, widget in self.widgets.items():
            value = widget.get()
            print(name, value, type(value))
        
        value = self.widgets["input"].get()
        self.update_results(value, float(value)/3)
        
        
    def update_results(self, fibunacci, time):
        self.widgets["fibunacci"].delete(0, tk.END)
        self.widgets["fibunacci"].insert(0, str(fibunacci))
        self.widgets["time"].delete(0, tk.END)
        self.widgets["time"].insert(0, str(time))
        


if __name__ == "__main__":
    app = App()
    app.mainloop()