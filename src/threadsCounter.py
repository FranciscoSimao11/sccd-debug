import counter
from sccd.runtime.statecharts_core import Event
import threading

if __name__ == '__main__':
    controller = counter.Controller()
    
    def raw_inputter():
        while 1:
            controller.addInput(Event(raw_input(), "input", []))
    input_thread = threading.Thread(target=raw_inputter)
    input_thread.daemon = True
    input_thread.start()
    
    output_listener = controller.addOutputListener(["output"])
    def outputter():
        while 1:
            print (output_listener.fetch(-1))
    output_thread = threading.Thread(target=outputter)
    output_thread.daemon = True
    output_thread.start()
    
    controller.start()