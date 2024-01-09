"""
Generated by Statechart compiler by Glenn De Jonghe, Joeri Exelmans, Simon Van Mierlo, and Yentl Van Tendeloo (for the inspiration)

Model author: Francisco Simoes
Model name:   Composite Counter

"""

from python_sccd.python_sccd_runtime.statecharts_core import *
from sccd.runtime.statecharts_core import *
import argparse

# package "Composite Counter"

class MainApp(RuntimeClassBase):
    def __init__(self, controller):
        RuntimeClassBase.__init__(self, controller)
        
        self.semantics.big_step_maximality = StatechartSemantics.TakeMany
        self.semantics.internal_event_lifeline = StatechartSemantics.Queue
        self.semantics.input_event_lifeline = StatechartSemantics.FirstComboStep
        self.semantics.priority = StatechartSemantics.SourceParent
        self.semantics.concurrency = StatechartSemantics.Single
        
        self.debugFlags = Queue()
        self.firstTime = True
        self.didCalcs = Queue()
        self.active_states = Queue()
        self.startTime = 0.0
        self.executionTime = 0.0
        self.localExecutionTime = 0.0
        self.cumulativeDebugTime = 0.0
        
        # set execution speed
        self.setSimulationSpeed()
        
        # build Statechart structure
        self.build_statechart_structure()
        
        # user defined attributes
        self.counter = 0
        
        # call user defined constructor
        MainApp.user_defined_constructor(self)
    
    def user_defined_constructor(self):
        pass
    
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
    def increment_counter(self):
        print(self.current_state.name)
        self.counter = self.counter + 1
        print ("counter: ", self.counter)
    
    
    # builds Statechart structure
    def build_statechart_structure(self):
        
        # state <root>
        self.states[""] = State(0, "", self)
        
        # state /parallel
        self.states["/parallel"] = ParallelState(1, "/parallel", self)
        self.states["/parallel"].setEnter(self._parallel_enter)
        self.states["/parallel"].setExit(self._parallel_exit)
        
        # state /parallel/state_A
        self.states["/parallel/state_A"] = State(2, "/parallel/state_A", self)
        self.states["/parallel/state_A"].setEnter(self._parallel_state_A_enter)
        self.states["/parallel/state_A"].setExit(self._parallel_state_A_exit)
        
        # state /parallel/state_A/state_A1
        self.states["/parallel/state_A/state_A1"] = State(3, "/parallel/state_A/state_A1", self)
        self.states["/parallel/state_A/state_A1"].setEnter(self._parallel_state_A_state_A1_enter)
        self.states["/parallel/state_A/state_A1"].setExit(self._parallel_state_A_state_A1_exit)
        
        # state /parallel/state_A/state_A2
        self.states["/parallel/state_A/state_A2"] = State(4, "/parallel/state_A/state_A2", self)
        self.states["/parallel/state_A/state_A2"].setEnter(self._parallel_state_A_state_A2_enter)
        self.states["/parallel/state_A/state_A2"].setExit(self._parallel_state_A_state_A2_exit)
        
        # state /parallel/state_B
        self.states["/parallel/state_B"] = State(5, "/parallel/state_B", self)
        self.states["/parallel/state_B"].setEnter(self._parallel_state_B_enter)
        self.states["/parallel/state_B"].setExit(self._parallel_state_B_exit)
        
        # state /parallel/state_B/state_B1
        self.states["/parallel/state_B/state_B1"] = State(6, "/parallel/state_B/state_B1", self)
        self.states["/parallel/state_B/state_B1"].setEnter(self._parallel_state_B_state_B1_enter)
        self.states["/parallel/state_B/state_B1"].setExit(self._parallel_state_B_state_B1_exit)
        
        # state /parallel/state_B/state_B2
        self.states["/parallel/state_B/state_B2"] = State(7, "/parallel/state_B/state_B2", self)
        self.states["/parallel/state_B/state_B2"].setEnter(self._parallel_state_B_state_B2_enter)
        self.states["/parallel/state_B/state_B2"].setExit(self._parallel_state_B_state_B2_exit)
        
        # state /state_C
        self.states["/state_C"] = State(8, "/state_C", self)
        self.states["/state_C"].setEnter(self._state_C_enter)
        self.states["/state_C"].setExit(self._state_C_exit)
        
        # state /state_Debug
        self.states["/state_Debug"] = State(9, "/state_Debug", self)
        self.states["/state_Debug"].setEnter(self._state_Debug_enter)
        self.states["/state_Debug"].setExit(self._state_Debug_exit)
        
        # debug events
        pauseEvent = Event("pause", self.getInPortName("input"))
        continueEvent = Event("continue", self.getInPortName("input"))
        
        # debug transitions
        self.pauseTransitions = {}
        self.timedTransitions = []
        self.eventTransitions = {}
        
        # add children
        self.states[""].addChild(self.states["/parallel"])
        self.states[""].addChild(self.states["/state_C"])
        self.states["/parallel"].addChild(self.states["/parallel/state_A"])
        self.states["/parallel"].addChild(self.states["/parallel/state_B"])
        self.states["/parallel/state_A"].addChild(self.states["/parallel/state_A/state_A1"])
        self.states["/parallel/state_A"].addChild(self.states["/parallel/state_A/state_A2"])
        self.states["/parallel/state_B"].addChild(self.states["/parallel/state_B/state_B1"])
        self.states["/parallel/state_B"].addChild(self.states["/parallel/state_B/state_B2"])
        self.states[""].addChild(self.states["/state_Debug"])
        self.states[""].fixTree()
        self.states[""].default_state = self.states["/parallel"]
        self.states["/parallel/state_A"].default_state = self.states["/parallel/state_A/state_A1"]
        self.states["/parallel/state_B"].default_state = self.states["/parallel/state_B/state_B1"]
        
        # transition /parallel/state_A/state_A1
        self.eventTransitions["/parallel/state_A/state_A1"] = []
        _parallel_state_A_state_A1_0 = Transition(self, self.states["/parallel/state_A/state_A1"], [self.states["/parallel/state_A/state_A2"]])
        _parallel_state_A_state_A1_0.setTrigger(Event("_0after"))
        self.states["/parallel/state_A/state_A1"].addTransition(_parallel_state_A_state_A1_0)
        self.timedTransitions.append(_parallel_state_A_state_A1_0)
        
        # transition /parallel/state_A/state_A2
        self.eventTransitions["/parallel/state_A/state_A2"] = []
        _parallel_state_A_state_A2_0 = Transition(self, self.states["/parallel/state_A/state_A2"], [self.states["/parallel/state_A/state_A1"]])
        _parallel_state_A_state_A2_0.setTrigger(Event("move", self.getInPortName("input")))
        self.states["/parallel/state_A/state_A2"].addTransition(_parallel_state_A_state_A2_0)
        self.eventTransitions["/parallel/state_A/state_A2"].append(_parallel_state_A_state_A2_0)
        
        # transition /parallel/state_B/state_B1
        self.eventTransitions["/parallel/state_B/state_B1"] = []
        _parallel_state_B_state_B1_0 = Transition(self, self.states["/parallel/state_B/state_B1"], [self.states["/parallel/state_B/state_B2"]])
        _parallel_state_B_state_B1_0.setTrigger(Event("_1after"))
        self.states["/parallel/state_B/state_B1"].addTransition(_parallel_state_B_state_B1_0)
        self.timedTransitions.append(_parallel_state_B_state_B1_0)
        
        # transition /parallel/state_B/state_B2
        self.eventTransitions["/parallel/state_B/state_B2"] = []
        _parallel_state_B_state_B2_0 = Transition(self, self.states["/parallel/state_B/state_B2"], [self.states["/parallel/state_B/state_B1"]])
        _parallel_state_B_state_B2_0.setTrigger(Event("move", self.getInPortName("input")))
        self.states["/parallel/state_B/state_B2"].addTransition(_parallel_state_B_state_B2_0)
        self.eventTransitions["/parallel/state_B/state_B2"].append(_parallel_state_B_state_B2_0)
        
        # transition /state_C
        self.eventTransitions["/state_C"] = []
        _state_C_0 = Transition(self, self.states["/state_C"], [self.states["/parallel"]])
        _state_C_0.setTrigger(Event("moveParallel", self.getInPortName("input")))
        self.states["/state_C"].addTransition(_state_C_0)
        self.eventTransitions["/state_C"].append(_state_C_0)
        
        # transitions /state_Debug
        # _parallel to /state_Debug
        _parallel_to_state_Debug = Transition(self, self.states["/parallel"], [self.states["/state_Debug"]])
        _parallel_to_state_Debug.setTrigger(pauseEvent)
        self.states["/parallel"].addTransition(_parallel_to_state_Debug)
        self.pauseTransitions["/parallel"] = _parallel_to_state_Debug
        
        # _parallel_state_A to /state_Debug
        _parallel_state_A_to_state_Debug = Transition(self, self.states["/parallel/state_A"], [self.states["/state_Debug"]])
        _parallel_state_A_to_state_Debug.setTrigger(pauseEvent)
        self.states["/parallel/state_A"].addTransition(_parallel_state_A_to_state_Debug)
        self.pauseTransitions["/parallel/state_A"] = _parallel_state_A_to_state_Debug
        
        # _parallel_state_A_state_A1 to /state_Debug
        _parallel_state_A_state_A1_to_state_Debug = Transition(self, self.states["/parallel/state_A/state_A1"], [self.states["/state_Debug"]])
        _parallel_state_A_state_A1_to_state_Debug.setTrigger(pauseEvent)
        self.states["/parallel/state_A/state_A1"].addTransition(_parallel_state_A_state_A1_to_state_Debug)
        self.pauseTransitions["/parallel/state_A/state_A1"] = _parallel_state_A_state_A1_to_state_Debug
        
        # _parallel_state_A_state_A2 to /state_Debug
        _parallel_state_A_state_A2_to_state_Debug = Transition(self, self.states["/parallel/state_A/state_A2"], [self.states["/state_Debug"]])
        _parallel_state_A_state_A2_to_state_Debug.setTrigger(pauseEvent)
        self.states["/parallel/state_A/state_A2"].addTransition(_parallel_state_A_state_A2_to_state_Debug)
        self.pauseTransitions["/parallel/state_A/state_A2"] = _parallel_state_A_state_A2_to_state_Debug
        
        # _parallel_state_B to /state_Debug
        _parallel_state_B_to_state_Debug = Transition(self, self.states["/parallel/state_B"], [self.states["/state_Debug"]])
        _parallel_state_B_to_state_Debug.setTrigger(pauseEvent)
        self.states["/parallel/state_B"].addTransition(_parallel_state_B_to_state_Debug)
        self.pauseTransitions["/parallel/state_B"] = _parallel_state_B_to_state_Debug
        
        # _parallel_state_B_state_B1 to /state_Debug
        _parallel_state_B_state_B1_to_state_Debug = Transition(self, self.states["/parallel/state_B/state_B1"], [self.states["/state_Debug"]])
        _parallel_state_B_state_B1_to_state_Debug.setTrigger(pauseEvent)
        self.states["/parallel/state_B/state_B1"].addTransition(_parallel_state_B_state_B1_to_state_Debug)
        self.pauseTransitions["/parallel/state_B/state_B1"] = _parallel_state_B_state_B1_to_state_Debug
        
        # _parallel_state_B_state_B2 to /state_Debug
        _parallel_state_B_state_B2_to_state_Debug = Transition(self, self.states["/parallel/state_B/state_B2"], [self.states["/state_Debug"]])
        _parallel_state_B_state_B2_to_state_Debug.setTrigger(pauseEvent)
        self.states["/parallel/state_B/state_B2"].addTransition(_parallel_state_B_state_B2_to_state_Debug)
        self.pauseTransitions["/parallel/state_B/state_B2"] = _parallel_state_B_state_B2_to_state_Debug
        
        # _state_C to /state_Debug
        _state_C_to_state_Debug = Transition(self, self.states["/state_C"], [self.states["/state_Debug"]])
        _state_C_to_state_Debug.setTrigger(pauseEvent)
        self.states["/state_C"].addTransition(_state_C_to_state_Debug)
        self.pauseTransitions["/state_C"] = _state_C_to_state_Debug
        
        varBreakpoint0 = Transition(self, self.states["/parallel"], [self.states["/state_Debug"]])
        varBreakpoint0.setTrigger(Event("_3after"))
        self.states["/parallel"].addTransition(varBreakpoint0)
        
        varBreakpoint1 = Transition(self, self.states["/parallel/state_A"], [self.states["/state_Debug"]])
        varBreakpoint1.setTrigger(Event("_3after"))
        self.states["/parallel/state_A"].addTransition(varBreakpoint1)
        
        varBreakpoint2 = Transition(self, self.states["/parallel/state_A/state_A1"], [self.states["/state_Debug"]])
        varBreakpoint2.setTrigger(Event("_3after"))
        self.states["/parallel/state_A/state_A1"].addTransition(varBreakpoint2)
        
        varBreakpoint3 = Transition(self, self.states["/parallel/state_A/state_A2"], [self.states["/state_Debug"]])
        varBreakpoint3.setTrigger(Event("_3after"))
        self.states["/parallel/state_A/state_A2"].addTransition(varBreakpoint3)
        
        varBreakpoint4 = Transition(self, self.states["/parallel/state_B"], [self.states["/state_Debug"]])
        varBreakpoint4.setTrigger(Event("_3after"))
        self.states["/parallel/state_B"].addTransition(varBreakpoint4)
        
        varBreakpoint5 = Transition(self, self.states["/parallel/state_B/state_B1"], [self.states["/state_Debug"]])
        varBreakpoint5.setTrigger(Event("_3after"))
        self.states["/parallel/state_B/state_B1"].addTransition(varBreakpoint5)
        
        varBreakpoint6 = Transition(self, self.states["/parallel/state_B/state_B2"], [self.states["/state_Debug"]])
        varBreakpoint6.setTrigger(Event("_3after"))
        self.states["/parallel/state_B/state_B2"].addTransition(varBreakpoint6)
        
        varBreakpoint7 = Transition(self, self.states["/state_C"], [self.states["/state_Debug"]])
        varBreakpoint7.setTrigger(Event("_3after"))
        self.states["/state_C"].addTransition(varBreakpoint7)
        
    
    def _parallel_enter(self):
        self.current_state = self.states["/parallel"]
        self.startTime = self.getSimulatedTime()
        
        if self.states["/parallel"].children == []:
            while (not self.didCalcs.empty()):
                self.didCalcs.get()
        if self.firstTime == True:
            self.localExecutionTime = 0.0
            if self.states["/parallel"].children == []:
                self.debugFlags.put(False)
                self.active_states.put(self.current_state)
            timers = []
            
            if self.counter == 5:
                self.addTimer(2, 0)
        else:
            if self.states["/parallel"].children == []:
                self.debugFlags.get()
                self.debugFlags.put(False)
    
    def _parallel_exit(self):
        if (self.states["/parallel"].children == []) and self.didCalcs.empty():
            self.localExecutionTime = (self.localExecutionTime + (self.getSimulatedTime() - self.startTime))
            self.executionTime = (self.executionTime + (self.getSimulatedTime() - self.startTime))
            self.didCalcs.put(True)
        if self.pauseTransitions["/parallel"].enabled_event == None:
            if self.states["/parallel"].children == []:
                self.debugFlags.get()
                self.firstTime = True
                self.active_states.get()
    
    def _parallel_state_A_enter(self):
        self.current_state = self.states["/parallel/state_A"]
        self.startTime = self.getSimulatedTime()
        
        if self.states["/parallel/state_A"].children == []:
            while (not self.didCalcs.empty()):
                self.didCalcs.get()
        if self.firstTime == True:
            self.localExecutionTime = 0.0
            if self.states["/parallel/state_A"].children == []:
                self.debugFlags.put(False)
                self.active_states.put(self.current_state)
            timers = []
            
            if self.counter == 5:
                self.addTimer(2, 0)
        else:
            if self.states["/parallel/state_A"].children == []:
                self.debugFlags.get()
                self.debugFlags.put(False)
    
    def _parallel_state_A_exit(self):
        if (self.states["/parallel/state_A"].children == []) and self.didCalcs.empty():
            self.localExecutionTime = (self.localExecutionTime + (self.getSimulatedTime() - self.startTime))
            self.executionTime = (self.executionTime + (self.getSimulatedTime() - self.startTime))
            self.didCalcs.put(True)
        if self.pauseTransitions["/parallel/state_A"].enabled_event == None:
            if self.states["/parallel/state_A"].children == []:
                self.debugFlags.get()
                self.firstTime = True
                self.active_states.get()
    
    def _parallel_state_B_enter(self):
        self.current_state = self.states["/parallel/state_B"]
        self.startTime = self.getSimulatedTime()
        
        if self.states["/parallel/state_B"].children == []:
            while (not self.didCalcs.empty()):
                self.didCalcs.get()
        if self.firstTime == True:
            self.localExecutionTime = 0.0
            if self.states["/parallel/state_B"].children == []:
                self.debugFlags.put(False)
                self.active_states.put(self.current_state)
            timers = []
            
            if self.counter == 5:
                self.addTimer(2, 0)
        else:
            if self.states["/parallel/state_B"].children == []:
                self.debugFlags.get()
                self.debugFlags.put(False)
    
    def _parallel_state_B_exit(self):
        if (self.states["/parallel/state_B"].children == []) and self.didCalcs.empty():
            self.localExecutionTime = (self.localExecutionTime + (self.getSimulatedTime() - self.startTime))
            self.executionTime = (self.executionTime + (self.getSimulatedTime() - self.startTime))
            self.didCalcs.put(True)
        if self.pauseTransitions["/parallel/state_B"].enabled_event == None:
            if self.states["/parallel/state_B"].children == []:
                self.debugFlags.get()
                self.firstTime = True
                self.active_states.get()
    
    def _parallel_state_A_state_A1_enter(self):
        self.current_state = self.states["/parallel/state_A/state_A1"]
        self.startTime = self.getSimulatedTime()
        
        if self.states["/parallel/state_A/state_A1"].children == []:
            while (not self.didCalcs.empty()):
                self.didCalcs.get()
        if self.firstTime == True:
            self.localExecutionTime = 0.0
            if self.states["/parallel/state_A/state_A1"].children == []:
                self.debugFlags.put(False)
                self.active_states.put(self.current_state)
            self.increment_counter();
            timers = []
            self.addTimer(0, 5 / self.scaleFactor)
            timers.append(5)
            iteration = 0
            chosen = None
            lowest = timers[0]
            for t in self.timedTransitions:
                port = t.trigger.port
                source = t.source.name
                if (source == self.current_state.name) and (port != "input"):
                    if lowest >= timers[iteration]:
                        lowest = timers[iteration]
                        chosen = t
                    iteration = iteration + 1
            if iteration > 0:
                temp = Transition(self, chosen.source, chosen.targets)
                temp.setTrigger(Event("step", self.getInPortName("input")))
                chosen.source.addTransition(temp)
                attrs = [s.name for s in chosen.targets]
                print("[time-based] type step to move to {} ".format(attrs))
            
            possibleT = self.eventTransitions["/parallel/state_A/state_A1"]
            source = self.current_state
            i = 0
            for t in possibleT:
                temp = Transition(self, source, t.targets)
                name = "step" + str(i)
                temp.setTrigger(Event(name, self.getInPortName("input")))
                source.addTransition(temp)
                attrs = [s.name for s in t.targets]
                print("[event-based] type {} to move to {} ".format(name, attrs))
                i = (i + 1)
            if self.counter == 5:
                self.addTimer(2, 0)
        else:
            if self.states["/parallel/state_A/state_A1"].children == []:
                self.debugFlags.get()
                self.debugFlags.put(False)
            self.addTimer(0, 5.0 - ((self.localExecutionTime / 1000.0) / self.scaleFactor))
    
    def _parallel_state_A_state_A1_exit(self):
        self.removeTimer(0)
        if (self.states["/parallel/state_A/state_A1"].children == []) and self.didCalcs.empty():
            self.localExecutionTime = (self.localExecutionTime + (self.getSimulatedTime() - self.startTime))
            self.executionTime = (self.executionTime + (self.getSimulatedTime() - self.startTime))
            self.didCalcs.put(True)
        if self.pauseTransitions["/parallel/state_A/state_A1"].enabled_event == None:
            if self.states["/parallel/state_A/state_A1"].children == []:
                self.debugFlags.get()
                self.firstTime = True
                self.active_states.get()
    
    def _parallel_state_A_state_A2_enter(self):
        self.current_state = self.states["/parallel/state_A/state_A2"]
        self.startTime = self.getSimulatedTime()
        
        if self.states["/parallel/state_A/state_A2"].children == []:
            while (not self.didCalcs.empty()):
                self.didCalcs.get()
        if self.firstTime == True:
            self.localExecutionTime = 0.0
            if self.states["/parallel/state_A/state_A2"].children == []:
                self.debugFlags.put(False)
                self.active_states.put(self.current_state)
            self.increment_counter();
            timers = []
            
            possibleT = self.eventTransitions["/parallel/state_A/state_A2"]
            source = self.current_state
            i = 0
            for t in possibleT:
                temp = Transition(self, source, t.targets)
                name = "step" + str(i)
                temp.setTrigger(Event(name, self.getInPortName("input")))
                source.addTransition(temp)
                attrs = [s.name for s in t.targets]
                print("[event-based] type {} to move to {} ".format(name, attrs))
                i = (i + 1)
            if self.counter == 5:
                self.addTimer(2, 0)
        else:
            if self.states["/parallel/state_A/state_A2"].children == []:
                self.debugFlags.get()
                self.debugFlags.put(False)
    
    def _parallel_state_A_state_A2_exit(self):
        if (self.states["/parallel/state_A/state_A2"].children == []) and self.didCalcs.empty():
            self.localExecutionTime = (self.localExecutionTime + (self.getSimulatedTime() - self.startTime))
            self.executionTime = (self.executionTime + (self.getSimulatedTime() - self.startTime))
            self.didCalcs.put(True)
        if self.pauseTransitions["/parallel/state_A/state_A2"].enabled_event == None:
            if self.states["/parallel/state_A/state_A2"].children == []:
                self.debugFlags.get()
                self.firstTime = True
                self.active_states.get()
    
    def _parallel_state_B_state_B1_enter(self):
        self.current_state = self.states["/parallel/state_B/state_B1"]
        self.startTime = self.getSimulatedTime()
        
        if self.states["/parallel/state_B/state_B1"].children == []:
            while (not self.didCalcs.empty()):
                self.didCalcs.get()
        if self.firstTime == True:
            self.localExecutionTime = 0.0
            if self.states["/parallel/state_B/state_B1"].children == []:
                self.debugFlags.put(False)
                self.active_states.put(self.current_state)
            self.increment_counter();
            timers = []
            self.addTimer(1, 5 / self.scaleFactor)
            timers.append(5)
            iteration = 0
            chosen = None
            lowest = timers[0]
            for t in self.timedTransitions:
                port = t.trigger.port
                source = t.source.name
                if (source == self.current_state.name) and (port != "input"):
                    if lowest >= timers[iteration]:
                        lowest = timers[iteration]
                        chosen = t
                    iteration = iteration + 1
            if iteration > 0:
                temp = Transition(self, chosen.source, chosen.targets)
                temp.setTrigger(Event("step", self.getInPortName("input")))
                chosen.source.addTransition(temp)
                attrs = [s.name for s in chosen.targets]
                print("[time-based] type step to move to {} ".format(attrs))
            
            possibleT = self.eventTransitions["/parallel/state_B/state_B1"]
            source = self.current_state
            i = 0
            for t in possibleT:
                temp = Transition(self, source, t.targets)
                name = "step" + str(i)
                temp.setTrigger(Event(name, self.getInPortName("input")))
                source.addTransition(temp)
                attrs = [s.name for s in t.targets]
                print("[event-based] type {} to move to {} ".format(name, attrs))
                i = (i + 1)
            if self.counter == 5:
                self.addTimer(2, 0)
        else:
            if self.states["/parallel/state_B/state_B1"].children == []:
                self.debugFlags.get()
                self.debugFlags.put(False)
            self.addTimer(1, 5.0 - ((self.localExecutionTime / 1000.0) / self.scaleFactor))
    
    def _parallel_state_B_state_B1_exit(self):
        self.removeTimer(1)
        if (self.states["/parallel/state_B/state_B1"].children == []) and self.didCalcs.empty():
            self.localExecutionTime = (self.localExecutionTime + (self.getSimulatedTime() - self.startTime))
            self.executionTime = (self.executionTime + (self.getSimulatedTime() - self.startTime))
            self.didCalcs.put(True)
        if self.pauseTransitions["/parallel/state_B/state_B1"].enabled_event == None:
            if self.states["/parallel/state_B/state_B1"].children == []:
                self.debugFlags.get()
                self.firstTime = True
                self.active_states.get()
    
    def _parallel_state_B_state_B2_enter(self):
        self.current_state = self.states["/parallel/state_B/state_B2"]
        self.startTime = self.getSimulatedTime()
        
        if self.states["/parallel/state_B/state_B2"].children == []:
            while (not self.didCalcs.empty()):
                self.didCalcs.get()
        if self.firstTime == True:
            self.localExecutionTime = 0.0
            if self.states["/parallel/state_B/state_B2"].children == []:
                self.debugFlags.put(False)
                self.active_states.put(self.current_state)
            self.increment_counter();
            timers = []
            
            possibleT = self.eventTransitions["/parallel/state_B/state_B2"]
            source = self.current_state
            i = 0
            for t in possibleT:
                temp = Transition(self, source, t.targets)
                name = "step" + str(i)
                temp.setTrigger(Event(name, self.getInPortName("input")))
                source.addTransition(temp)
                attrs = [s.name for s in t.targets]
                print("[event-based] type {} to move to {} ".format(name, attrs))
                i = (i + 1)
            if self.counter == 5:
                self.addTimer(2, 0)
        else:
            if self.states["/parallel/state_B/state_B2"].children == []:
                self.debugFlags.get()
                self.debugFlags.put(False)
    
    def _parallel_state_B_state_B2_exit(self):
        if (self.states["/parallel/state_B/state_B2"].children == []) and self.didCalcs.empty():
            self.localExecutionTime = (self.localExecutionTime + (self.getSimulatedTime() - self.startTime))
            self.executionTime = (self.executionTime + (self.getSimulatedTime() - self.startTime))
            self.didCalcs.put(True)
        if self.pauseTransitions["/parallel/state_B/state_B2"].enabled_event == None:
            if self.states["/parallel/state_B/state_B2"].children == []:
                self.debugFlags.get()
                self.firstTime = True
                self.active_states.get()
    
    def _state_C_enter(self):
        self.current_state = self.states["/state_C"]
        self.startTime = self.getSimulatedTime()
        
        if self.states["/state_C"].children == []:
            while (not self.didCalcs.empty()):
                self.didCalcs.get()
        if self.firstTime == True:
            self.localExecutionTime = 0.0
            if self.states["/state_C"].children == []:
                self.debugFlags.put(False)
                self.active_states.put(self.current_state)
            self.increment_counter();
            timers = []
            
            possibleT = self.eventTransitions["/state_C"]
            source = self.current_state
            i = 0
            for t in possibleT:
                temp = Transition(self, source, t.targets)
                name = "step" + str(i)
                temp.setTrigger(Event(name, self.getInPortName("input")))
                source.addTransition(temp)
                attrs = [s.name for s in t.targets]
                print("[event-based] type {} to move to {} ".format(name, attrs))
                i = (i + 1)
            if self.counter == 5:
                self.addTimer(2, 0)
        else:
            if self.states["/state_C"].children == []:
                self.debugFlags.get()
                self.debugFlags.put(False)
    
    def _state_C_exit(self):
        if (self.states["/state_C"].children == []) and self.didCalcs.empty():
            self.localExecutionTime = (self.localExecutionTime + (self.getSimulatedTime() - self.startTime))
            self.executionTime = (self.executionTime + (self.getSimulatedTime() - self.startTime))
            self.didCalcs.put(True)
        if self.pauseTransitions["/state_C"].enabled_event == None:
            if self.states["/state_C"].children == []:
                self.debugFlags.get()
                self.firstTime = True
                self.active_states.get()
    
    def _state_Debug_enter(self):
        if self.firstTime:
            self.firstTime = False
        nFlags = 0
        while (not self.debugFlags.empty()):
            self.debugFlags.get()
            nFlags = (nFlags + 1)
        for x in range(nFlags):
            self.debugFlags.put(True)
        targets = list(self.active_states.queue)
        source = self.states["/state_Debug"]
        newTransition = Transition(self, source, targets)
        newTransition.setTrigger(Event("continue", self.getInPortName("input")))
        source.addTransition(newTransition)
        
        print("DEBUG MODE")
        print("Current State: ", self.current_state.name)
        print("counter: ", self.counter)
    
    def _state_Debug_exit(self):
        self.cumulativeDebugTime = (self.getSimulatedTime() - self.executionTime)
        targets = list(self.active_states.queue)
        for t in targets:
            self.pauseTransitions[t.name].enabled_event = None
    
    def continueGuard_parallel(self, parameters):
        return self.current_state == self.states["/parallel"]
    
    def continueGuard_parallel_state_A(self, parameters):
        return self.current_state == self.states["/parallel/state_A"]
    
    def continueGuard_parallel_state_A_state_A1(self, parameters):
        return self.current_state == self.states["/parallel/state_A/state_A1"]
    
    def continueGuard_parallel_state_A_state_A2(self, parameters):
        return self.current_state == self.states["/parallel/state_A/state_A2"]
    
    def continueGuard_parallel_state_B(self, parameters):
        return self.current_state == self.states["/parallel/state_B"]
    
    def continueGuard_parallel_state_B_state_B1(self, parameters):
        return self.current_state == self.states["/parallel/state_B/state_B1"]
    
    def continueGuard_parallel_state_B_state_B2(self, parameters):
        return self.current_state == self.states["/parallel/state_B/state_B2"]
    
    def continueGuard_state_C(self, parameters):
        return self.current_state == self.states["/state_C"]
    
    def initializeStatechart(self):
        # enter default state
        self.default_targets = self.states["/parallel"].getEffectiveTargetStates()
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

class Controller(ThreadsControllerBase):
    def __init__(self, keep_running = None, behind_schedule_callback = None):
        if keep_running == None: keep_running = True
        if behind_schedule_callback == None: behind_schedule_callback = None
        ThreadsControllerBase.__init__(self, ObjectManager(self), keep_running, behind_schedule_callback)
        self.addInputPort("input")
        self.addOutputPort("output")
        self.object_manager.createInstance("MainApp", [])