import logging, time, threading, typing
import tkinter as tk
from collections import OrderedDict

PADX, PADY = 5, 3      # Widget padding

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s | %(threadName)12s | %(message)s')

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
        self.buttons["worker"] = tk.Button(self.frames["lower"], text="compute in worker thread", command=self.on_button_worker)
        for column, button in enumerate(self.buttons.values()):
            button.grid(row=0, column=column, padx=PADX, pady=PADY)
            
        self.worker = Worker(self.update_results)
        self.worker.start()
            
            
    def on_button_main(self):
        fib, t = calc_fibunacci(int(self.widgets["input"].get()))
        self.update_results(fib, t)
        
        
    def on_button_worker(self):
        self.worker.compute_inputs.append(int(self.widgets["input"].get()))
        
        
    def update_results(self, fibunacci, t):
        logging.debug(f"updating {fibunacci=}, {t=}")
        self.widgets["fibunacci"].delete(0, tk.END)
        self.widgets["fibunacci"].insert(0, str(fibunacci))
        self.widgets["time"].delete(0, tk.END)
        self.widgets["time"].insert(0, str(t))


class Worker(threading.Thread):
    def __init__(self, callback: typing.Callable):
        super().__init__()
        self.exiting = False              # kill thread by setting exiting=True
        self.compute_inputs = []
        self.callback = callback


    def run(self):
        logging.info("Starting thread")
        previous_beakon = 0
        beakon_period = 5
        while not self.exiting:
            if previous_beakon + beakon_period < time.time():
                previous_beakon = time.time()
                logging.debug("Thread is running")
                
            if len(self.compute_inputs):
                fib, t = calc_fibunacci(self.compute_inputs.pop())
                self.callback(fib, t)
                
            time.sleep(1e-4)
            
        logging.info("Exiting thread")
            

def calc_fibunacci(z: int) -> list:
    """
    Dummy load: Calculates the fibunacci number of z.
                Also measures the computation time.
    """
    def _calc_fib(z: int) -> float:
        """ Recursive fibunacci calculator
        """
        if z in (0, 1):
            return 1
        return _calc_fib(z-2) + _calc_fib(z-1)
    
    logging.debug(f"calculating for {z=}")
    t0 = time.time()
    res = _calc_fib(z)
    compute_time = time.time()-t0
    return [res, compute_time]


if __name__ == "__main__":
    app = App()
    app.mainloop()