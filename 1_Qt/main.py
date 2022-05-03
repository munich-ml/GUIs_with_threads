# -*- coding: utf-8 -*-


import sys
import time
from Gui import Ui_demo
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QThread, pyqtSignal


class QThreadDemo(QMainWindow, Ui_demo):
    """
    Simple Qt Application demonstrating the usage of a QThread
    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.buttonCalcMain.clicked.connect(self.on_button_calc_main)
        self.buttonCalcWorker.clicked.connect(self.on_button_calc_worker)

        self.worker = Worker()
        self.worker.signalResultReady.connect(self.show_new_result)
        self.worker.start()        # start the worker thread


    def on_button_calc_main(self):
        """
        calculate fibunacci in main thread
        """
        fib = calc_fibunacci(self.spinBoxInput.value())
        self.show_new_result(fib)


    def on_button_calc_worker(self):
        """
        calculate fibunacci in worker thread
        """
        self.worker.computeJobs.append(self.spinBoxInput.value())


    def show_new_result(self, result):
        fib, t = result
        self.lineEditResult.setText(str(fib))
        self.lineEditTime.setText(str(t))


class Worker(QThread):
    signalResultReady = pyqtSignal(list)  

    def __init__(self):
        super().__init__()
        self.exiting = False              # kill thread by setting exiting=True
        self.computeJobs = []


    def run(self):
        while not self.exiting:
            if len(self.computeJobs):
                fib = calc_fibunacci(self.computeJobs.pop())
                self.signalResultReady.emit(fib)
            time.sleep(1e-4)


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
    
    t0 = time.time()
    res = _calc_fib(z)
    computeTime = time.time()-t0
    return [res, computeTime]


if __name__ == '__main__':
    app = QApplication(sys.argv)
    qthreadDemo = QThreadDemo()
    qthreadDemo.show()
    app.exec_()
