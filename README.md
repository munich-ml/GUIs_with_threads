# QThread-demo-app
Qt application demonstrating the usage of QThreads

## Static UI with Qt Designer
- **Gui.ui** is the user interface definition, designed with the Qt Designer. 
- It is a static UI, meaning the widgets don't change during execution.
- **Gui.py** is the auto-generated python code of the user interface definiton.
- **toPy.bat** contains the command for compiling Gui.py from Gui.ui.
- **Don't edit Gui.py!** It is auto-generated and changes will be overwritten with the next compilation. 

## Application main.py
- Executing **main.py** launches a QApplication with **QThreadDemo** as the main window (the one and only).
- The **QThreadDemo** connects the UI elements.
- **QThreadDemo** also executes the load (**calc_fibunacci**) directly, meaning in the same thread. Thus, the GUI freezes while **calc_fibunacci** is calculating.
- Finally, **QThreadDemo** creates, connects and starts a **Worker** instance, which subclasses **QThread**.
- Tasks executed within the **Worker.run()** method run in a seperate thread, thus mostly independent of the main thread and therefore no GUI freeze.

## Connections between the threads
- **Main-->Worker**: Direct connection: Worker.computeJobs list.
- **Worker-->Main**: pyqtSignal: Worker.signalResultReady.

## Dummy laod: Fibunacci calculation
- **\_calc_fib** function calculates a fibunacci number. It's a nice dummy load, because the computation time scales exponentially with the input *z*. It is about a second for *z=33*.
- **calc_fibunacci** is just a wrapper around **\_calc_fib** which measures the computation time.


