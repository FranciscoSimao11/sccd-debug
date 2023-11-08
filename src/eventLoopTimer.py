import Tkinter as tk
import timer
import originalTimer
from sccd.runtime.libs.ui import ui
from sccd.runtime.statecharts_core import Event
from sccd.runtime.tkinter_eventloop import *

if __name__ == '__main__':
	ui.window = tk.Tk()

	controller = timer.Controller(TkEventLoop(ui.window))
	controller.start()
	#controller.run()
	ui.window.mainloop()
