"""
Generated by Statechart compiler by Glenn De Jonghe, Joeri Exelmans, Simon Van Mierlo, and Yentl Van Tendeloo (for the inspiration)

Model author: Simon Van Mierlo
Model name:   Timer (Eventloop Version)

"""

from python_sccd.python_sccd_runtime.statecharts_core import *
from sccd.runtime.statecharts_core import *
import argparse
from sccd.runtime.libs.ui import ui
import sccd.runtime.accurate_time

# package "Timer (Eventloop Version)"

class MainApp(RuntimeClassBase):
    def __init__(self, controller):
        RuntimeClassBase.__init__(self, controller)
        
        self.semantics.big_step_maximality = StatechartSemantics.TakeMany
        self.semantics.internal_event_lifeline = StatechartSemantics.Queue
        self.semantics.input_event_lifeline = StatechartSemantics.FirstComboStep
        self.semantics.priority = StatechartSemantics.SourceParent
        self.semantics.concurrency = StatechartSemantics.Single
        
        self.debugFlag = False
        self.startTime = 0
        self.timeDiff = 0
        
        # set execution speed
        self.setSimulationSpeed()
        
        # build Statechart structure
        self.build_statechart_structure()
        
        # call user defined constructor
        MainApp.user_defined_constructor(self)
    
    def user_defined_constructor(self):
        self.canvas = ui.append_canvas(ui.window,100,100,{'background':'#eee'})
        self.clock_text = self.canvas.element.create_text(25,25,{'text':'0.0'})
        self.actual_clock_text = self.canvas.element.create_text(25,50,{'text':'0.0'})
        interrupt_button = ui.append_button(ui.window, 'INTERRUPT');
        continue_button = ui.append_button(ui.window, 'CONTINUE');
        ui.bind_event(interrupt_button.element, ui.EVENTS.MOUSE_CLICK, self.controller, 'interrupt_clicked');
        ui.bind_event(continue_button.element, ui.EVENTS.MOUSE_CLICK, self.controller, 'continue_clicked');
    
    def setSimulationSpeed(self):
        
        parser = argparse.ArgumentParser(prog="python -m sccd.compiler.sccdc")
        parser.add_argument('-s','--simType', help='Simulation type which has 3 different variations: 0 = default simulation, scale factor of 1; 1 = scaled real-time simulation, takes one extra arg to set the scale factor; 2 = as-fast-as-possible simulation, scale factor = infinity', default=0)
        parser.add_argument('-f','--factor', help='Scale factor: default value is 1; if the factor is 2, the simulation 2x faster', default=1)
        args = vars(parser.parse_args())
        
        if args['simType'] is not None:
            args['simType'] = float(args['simType'])
            args['factor'] = float(args['factor'])
            if args['simType'] == 0:
                print("Real-time Simulation")
                self.scaleFactor = 1.0
            elif args['simType'] == 1:
                print("Scaled Real-time Simulation")
                if args['factor'] is not None and args['factor'] > 0:
                    self.scaleFactor = args['factor']
            elif args['simType'] == 2:
                print("As-fast-as-possible Simulation")
                self.scaleFactor = float('inf')
            else:
                print("Invalid simulation type. Defaulting to Real-time Simulation")
                self.scaleFactor = 1.0
            print("Scale Factor: {}".format(self.scaleFactor))
    
    def user_defined_destructor(self):
        pass
    
    
    # user defined method
    def update_timers(self):
        print(self.current_state.name)
        self.canvas.element.itemconfigure(self.clock_text, text=str('%.2f' % (self.getSimulatedTime() / 1000.0)))
        self.canvas.element.itemconfigure(self.actual_clock_text, text='%.2f' % (time() / 1000.0))
    
    
    # builds Statechart structure
    def build_statechart_structure(self):
        
        # state <root>
        self.states[""] = State(0, "", self)
        
        # state /running
        self.states["/running"] = State(1, "/running", self)
        self.states["/running"].setEnter(self._running_enter)
        self.states["/running"].setExit(self._running_exit)
        
        # state /interrupted
        self.states["/interrupted"] = State(2, "/interrupted", self)
        self.states["/interrupted"].setEnter(self._interrupted_enter)
        self.states["/interrupted"].setExit(self._interrupted_exit)
        
        # state /state_Debug
        self.states["/state_Debug"] = State(3, "/state_Debug", self)
        self.states["/state_Debug"].setEnter(self._state_Debug_enter)
        
        # debug events
        pauseEvent = Event("pause", self.getInPortName("input"))
        continueEvent = Event("continue", self.getInPortName("input"))
        
        # debug transitions
        self.pauseTransitions = {}
        
        # add children
        self.states[""].addChild(self.states["/running"])
        self.states[""].addChild(self.states["/interrupted"])
        self.states[""].addChild(self.states["/state_Debug"])
        self.states[""].fixTree()
        self.states[""].default_state = self.states["/running"]
        
        # transition /running
        _running_0 = Transition(self, self.states["/running"], [self.states["/running"]])
        _running_0.setAction(self._running_0_exec)
        _running_0.setTrigger(Event("_0after"))
        self.states["/running"].addTransition(_running_0)
        _running_1 = Transition(self, self.states["/running"], [self.states["/interrupted"]])
        _running_1.setAction(self._running_1_exec)
        _running_1.setTrigger(Event("interrupt_clicked", self.getInPortName("ui")))
        self.states["/running"].addTransition(_running_1)
        
        # transition /interrupted
        _interrupted_0 = Transition(self, self.states["/interrupted"], [self.states["/interrupted"]])
        _interrupted_0.setAction(self._interrupted_0_exec)
        _interrupted_0.setTrigger(Event("interrupt_clicked", self.getInPortName("ui")))
        self.states["/interrupted"].addTransition(_interrupted_0)
        _interrupted_1 = Transition(self, self.states["/interrupted"], [self.states["/running"]])
        _interrupted_1.setAction(self._interrupted_1_exec)
        _interrupted_1.setTrigger(Event("continue_clicked", self.getInPortName("ui")))
        self.states["/interrupted"].addTransition(_interrupted_1)
        
        # transitions /state_Debug
        # to /state_Debug
        _running_to_state_Debug = Transition(self, self.states["/running"], [self.states["/state_Debug"]])
        _running_to_state_Debug.setTrigger(pauseEvent)
        self.states["/running"].addTransition(_running_to_state_Debug)
        self.pauseTransitions["/running"] = _running_to_state_Debug
        
        # from /state_Debug
        _state_Debug_to_running = Transition(self, self.states["/state_Debug"], [self.states["/running"]])
        _state_Debug_to_running.setTrigger(continueEvent)
        _state_Debug_to_running.setGuard(self.continueGuard_running)
        self.states["/state_Debug"].addTransition(_state_Debug_to_running)
        
        # to /state_Debug
        _interrupted_to_state_Debug = Transition(self, self.states["/interrupted"], [self.states["/state_Debug"]])
        _interrupted_to_state_Debug.setTrigger(pauseEvent)
        self.states["/interrupted"].addTransition(_interrupted_to_state_Debug)
        self.pauseTransitions["/interrupted"] = _interrupted_to_state_Debug
        
        # from /state_Debug
        _state_Debug_to_interrupted = Transition(self, self.states["/state_Debug"], [self.states["/interrupted"]])
        _state_Debug_to_interrupted.setTrigger(continueEvent)
        _state_Debug_to_interrupted.setGuard(self.continueGuard_interrupted)
        self.states["/state_Debug"].addTransition(_state_Debug_to_interrupted)
        
    
    def _running_enter(self):
        self.current_state = self.states["/running"]
        self.startTime = self.getSimulatedTime()
        if self.debugFlag == False:
            self.addTimer(0, 0.05 / self.scaleFactor)
        else:
            if self.states["/running"].children == []:
                self.debugFlag = False
            self.addTimer(0, 0.05 - (self.timeDiff / self.scaleFactor))
    
    def _running_exit(self):
        self.removeTimer(0)
        if self.pauseTransitions["/running"].enabled_event == None:
            pass
    
    def _interrupted_enter(self):
        self.current_state = self.states["/interrupted"]
        self.startTime = self.getSimulatedTime()
        if self.debugFlag == False:
            pass
        else:
            if self.states["/interrupted"].children == []:
                self.debugFlag = False
    
    def _interrupted_exit(self):
        if self.pauseTransitions["/interrupted"].enabled_event == None:
            pass
    
    def _state_Debug_enter(self):
        self.timeDiff = ((self.getSimulatedTime() - self.startTime) / 1000.0)
        self.debugFlag = True
        print("DEBUG MODE")
        print("Current State: ", self.current_state.name)
    
    def _running_0_exec(self, parameters):
        self.update_timers()
    
    def _running_1_exec(self, parameters):
        self.update_timers()
    
    def _interrupted_0_exec(self, parameters):
        self.update_timers()
    
    def _interrupted_1_exec(self, parameters):
        self.update_timers()
    
    def continueGuard_running(self, parameters):
        return self.current_state == self.states["/running"]
    
    def continueGuard_interrupted(self, parameters):
        return self.current_state == self.states["/interrupted"]
    
    def initializeStatechart(self):
        # enter default state
        self.default_targets = self.states["/running"].getEffectiveTargetStates()
        RuntimeClassBase.initializeStatechart(self)

class ObjectManager(ObjectManagerBase):
    def __init__(self, controller):
        ObjectManagerBase.__init__(self, controller)
    
    def instantiate(self, class_name, construct_params):
        if class_name == "MainApp":
            instance = MainApp(self.controller)
            instance.associations = {}
        else:
            raise Exception("Cannot instantiate class " + class_name)
        return instance

class Controller(EventLoopControllerBase):
    def __init__(self, event_loop_callbacks, finished_callback = None, behind_schedule_callback = None):
        if finished_callback == None: finished_callback = None
        if behind_schedule_callback == None: behind_schedule_callback = None
        EventLoopControllerBase.__init__(self, ObjectManager(self), event_loop_callbacks, finished_callback, behind_schedule_callback)
        self.addInputPort("ui")
        self.object_manager.createInstance("MainApp", [])