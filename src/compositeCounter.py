"""
Generated by Statechart compiler by Glenn De Jonghe, Joeri Exelmans, Simon Van Mierlo, and Yentl Van Tendeloo (for the inspiration)

Model author: Francisco Simoes
Model name:   Counter

"""

from python_sccd.python_sccd_runtime.statecharts_core import *
from sccd.runtime.statecharts_core import *
import argparse

# package "Counter"

class MainApp(RuntimeClassBase):
    def __init__(self, controller):
        RuntimeClassBase.__init__(self, controller)
        
        self.semantics.big_step_maximality = StatechartSemantics.TakeMany
        self.semantics.internal_event_lifeline = StatechartSemantics.Queue
        self.semantics.input_event_lifeline = StatechartSemantics.FirstComboStep
        self.semantics.priority = StatechartSemantics.SourceParent
        self.semantics.concurrency = StatechartSemantics.Single
        
        self.debugFlag = False
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
        
        # state /state_A
        self.states["/state_A"] = State(1, "/state_A", self)
        self.states["/state_A"].setEnter(self._state_A_enter)
        self.states["/state_A"].setExit(self._state_A_exit)
        
        # state /state_A/state_A1
        self.states["/state_A/state_A1"] = State(2, "/state_A/state_A1", self)
        self.states["/state_A/state_A1"].setEnter(self._state_A_state_A1_enter)
        self.states["/state_A/state_A1"].setExit(self._state_A_state_A1_exit)
        
        # state /state_A/state_A2
        self.states["/state_A/state_A2"] = State(3, "/state_A/state_A2", self)
        self.states["/state_A/state_A2"].setEnter(self._state_A_state_A2_enter)
        self.states["/state_A/state_A2"].setExit(self._state_A_state_A2_exit)
        
        # state /state_B
        self.states["/state_B"] = State(4, "/state_B", self)
        self.states["/state_B"].setEnter(self._state_B_enter)
        self.states["/state_B"].setExit(self._state_B_exit)
        
        # state /state_Debug
        self.states["/state_Debug"] = State(5, "/state_Debug", self)
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
        self.states[""].addChild(self.states["/state_A"])
        self.states[""].addChild(self.states["/state_B"])
        self.states["/state_A"].addChild(self.states["/state_A/state_A1"])
        self.states["/state_A"].addChild(self.states["/state_A/state_A2"])
        self.states[""].addChild(self.states["/state_Debug"])
        self.states[""].fixTree()
        self.states[""].default_state = self.states["/state_A"]
        self.states["/state_A"].default_state = self.states["/state_A/state_A1"]
        
        # transition /state_A/state_A1
        self.eventTransitions["/state_A/state_A1"] = []
        _state_A_state_A1_0 = Transition(self, self.states["/state_A/state_A1"], [self.states["/state_A/state_A2"]])
        _state_A_state_A1_0.setTrigger(Event("a2", self.getInPortName("input")))
        self.states["/state_A/state_A1"].addTransition(_state_A_state_A1_0)
        self.eventTransitions["/state_A/state_A1"].append(_state_A_state_A1_0)
        _state_A_state_A1_1 = Transition(self, self.states["/state_A/state_A1"], [self.states["/state_A/state_A2"]])
        _state_A_state_A1_1.setTrigger(Event("_0after"))
        self.states["/state_A/state_A1"].addTransition(_state_A_state_A1_1)
        self.timedTransitions.append(_state_A_state_A1_1)
        
        # transition /state_A/state_A2
        self.eventTransitions["/state_A/state_A2"] = []
        _state_A_state_A2_0 = Transition(self, self.states["/state_A/state_A2"], [self.states["/state_A/state_A1"]])
        _state_A_state_A2_0.setTrigger(Event("a1", self.getInPortName("input")))
        self.states["/state_A/state_A2"].addTransition(_state_A_state_A2_0)
        self.eventTransitions["/state_A/state_A2"].append(_state_A_state_A2_0)
        _state_A_state_A2_1 = Transition(self, self.states["/state_A/state_A2"], [self.states["/state_B"]])
        _state_A_state_A2_1.setTrigger(Event("b", self.getInPortName("input")))
        self.states["/state_A/state_A2"].addTransition(_state_A_state_A2_1)
        self.eventTransitions["/state_A/state_A2"].append(_state_A_state_A2_1)
        
        # transition /state_B
        self.eventTransitions["/state_B"] = []
        _state_B_0 = Transition(self, self.states["/state_B"], [self.states["/state_A"]])
        _state_B_0.setTrigger(Event("move", self.getInPortName("input")))
        self.states["/state_B"].addTransition(_state_B_0)
        self.eventTransitions["/state_B"].append(_state_B_0)
        
        # transitions /state_Debug
        # _state_A to /state_Debug
        _state_A_to_state_Debug = Transition(self, self.states["/state_A"], [self.states["/state_Debug"]])
        _state_A_to_state_Debug.setTrigger(pauseEvent)
        self.states["/state_A"].addTransition(_state_A_to_state_Debug)
        self.pauseTransitions["/state_A"] = _state_A_to_state_Debug
        
        # state_A from /state_Debug
        _state_Debug_to_state_A = Transition(self, self.states["/state_Debug"], [self.states["/state_A"]])
        _state_Debug_to_state_A.setTrigger(continueEvent)
        _state_Debug_to_state_A.setGuard(self.continueGuard_state_A)
        self.states["/state_Debug"].addTransition(_state_Debug_to_state_A)
        
        # _state_A_state_A1 to /state_Debug
        _state_A_state_A1_to_state_Debug = Transition(self, self.states["/state_A/state_A1"], [self.states["/state_Debug"]])
        _state_A_state_A1_to_state_Debug.setTrigger(pauseEvent)
        self.states["/state_A/state_A1"].addTransition(_state_A_state_A1_to_state_Debug)
        self.pauseTransitions["/state_A/state_A1"] = _state_A_state_A1_to_state_Debug
        
        # state_A_state_A1 from /state_Debug
        _state_Debug_to_state_A_state_A1 = Transition(self, self.states["/state_Debug"], [self.states["/state_A/state_A1"]])
        _state_Debug_to_state_A_state_A1.setTrigger(continueEvent)
        _state_Debug_to_state_A_state_A1.setGuard(self.continueGuard_state_A_state_A1)
        self.states["/state_Debug"].addTransition(_state_Debug_to_state_A_state_A1)
        
        # _state_A_state_A2 to /state_Debug
        _state_A_state_A2_to_state_Debug = Transition(self, self.states["/state_A/state_A2"], [self.states["/state_Debug"]])
        _state_A_state_A2_to_state_Debug.setTrigger(pauseEvent)
        self.states["/state_A/state_A2"].addTransition(_state_A_state_A2_to_state_Debug)
        self.pauseTransitions["/state_A/state_A2"] = _state_A_state_A2_to_state_Debug
        
        # state_A_state_A2 from /state_Debug
        _state_Debug_to_state_A_state_A2 = Transition(self, self.states["/state_Debug"], [self.states["/state_A/state_A2"]])
        _state_Debug_to_state_A_state_A2.setTrigger(continueEvent)
        _state_Debug_to_state_A_state_A2.setGuard(self.continueGuard_state_A_state_A2)
        self.states["/state_Debug"].addTransition(_state_Debug_to_state_A_state_A2)
        
        # _state_B to /state_Debug
        _state_B_to_state_Debug = Transition(self, self.states["/state_B"], [self.states["/state_Debug"]])
        _state_B_to_state_Debug.setTrigger(pauseEvent)
        self.states["/state_B"].addTransition(_state_B_to_state_Debug)
        self.pauseTransitions["/state_B"] = _state_B_to_state_Debug
        
        # state_B from /state_Debug
        _state_Debug_to_state_B = Transition(self, self.states["/state_Debug"], [self.states["/state_B"]])
        _state_Debug_to_state_B.setTrigger(continueEvent)
        _state_Debug_to_state_B.setGuard(self.continueGuard_state_B)
        self.states["/state_Debug"].addTransition(_state_Debug_to_state_B)
        
        varBreakpoint0 = Transition(self, self.states["/state_A"], [self.states["/state_Debug"]])
        varBreakpoint0.setTrigger(Event("_2after"))
        self.states["/state_A"].addTransition(varBreakpoint0)
        
        varBreakpoint1 = Transition(self, self.states["/state_A/state_A1"], [self.states["/state_Debug"]])
        varBreakpoint1.setTrigger(Event("_2after"))
        self.states["/state_A/state_A1"].addTransition(varBreakpoint1)
        
        varBreakpoint2 = Transition(self, self.states["/state_A/state_A2"], [self.states["/state_Debug"]])
        varBreakpoint2.setTrigger(Event("_2after"))
        self.states["/state_A/state_A2"].addTransition(varBreakpoint2)
        
        varBreakpoint3 = Transition(self, self.states["/state_B"], [self.states["/state_Debug"]])
        varBreakpoint3.setTrigger(Event("_2after"))
        self.states["/state_B"].addTransition(varBreakpoint3)
        
    
    def _state_A_enter(self):
        self.current_state = self.states["/state_A"]
        self.startTime = self.getSimulatedTime()
        
        if self.debugFlag == False:
            self.localExecutionTime = 0.0
            timers = []
            
            if self.counter == 5:
                self.addTimer(1, 0)
        else:
            if self.states["/state_A"].children == []:
                self.debugFlag = False
    
    def _state_A_exit(self):
        if self.states["/state_A"].children == []:
            self.localExecutionTime = (self.localExecutionTime + (self.getSimulatedTime() - self.startTime))
            self.executionTime = (self.executionTime + (self.getSimulatedTime() - self.startTime))
        if self.pauseTransitions["/state_A"].enabled_event == None:
            self.increment_counter();
    
    def _state_A_state_A1_enter(self):
        self.current_state = self.states["/state_A/state_A1"]
        self.startTime = self.getSimulatedTime()
        
        if self.debugFlag == False:
            self.localExecutionTime = 0.0
            self.increment_counter();
            timers = []
            self.addTimer(0, 10 / self.scaleFactor)
            timers.append(10)
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
            
            possibleT = self.eventTransitions["/state_A/state_A1"]
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
                self.addTimer(1, 0)
        else:
            if self.states["/state_A/state_A1"].children == []:
                self.debugFlag = False
            self.addTimer(0, 10.0 - ((self.localExecutionTime / 1000.0) / self.scaleFactor))
    
    def _state_A_state_A1_exit(self):
        self.removeTimer(0)
        if self.states["/state_A/state_A1"].children == []:
            self.localExecutionTime = (self.localExecutionTime + (self.getSimulatedTime() - self.startTime))
            self.executionTime = (self.executionTime + (self.getSimulatedTime() - self.startTime))
        if self.pauseTransitions["/state_A/state_A1"].enabled_event == None:
            self.increment_counter();
    
    def _state_A_state_A2_enter(self):
        self.current_state = self.states["/state_A/state_A2"]
        self.startTime = self.getSimulatedTime()
        
        if self.debugFlag == False:
            self.localExecutionTime = 0.0
            self.increment_counter();
            timers = []
            
            possibleT = self.eventTransitions["/state_A/state_A2"]
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
                self.addTimer(1, 0)
        else:
            if self.states["/state_A/state_A2"].children == []:
                self.debugFlag = False
    
    def _state_A_state_A2_exit(self):
        if self.states["/state_A/state_A2"].children == []:
            self.localExecutionTime = (self.localExecutionTime + (self.getSimulatedTime() - self.startTime))
            self.executionTime = (self.executionTime + (self.getSimulatedTime() - self.startTime))
        if self.pauseTransitions["/state_A/state_A2"].enabled_event == None:
            pass
    
    def _state_B_enter(self):
        self.current_state = self.states["/state_B"]
        self.startTime = self.getSimulatedTime()
        
        if self.debugFlag == False:
            self.localExecutionTime = 0.0
            self.increment_counter();
            timers = []
            
            possibleT = self.eventTransitions["/state_B"]
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
                self.addTimer(1, 0)
        else:
            if self.states["/state_B"].children == []:
                self.debugFlag = False
    
    def _state_B_exit(self):
        if self.states["/state_B"].children == []:
            self.localExecutionTime = (self.localExecutionTime + (self.getSimulatedTime() - self.startTime))
            self.executionTime = (self.executionTime + (self.getSimulatedTime() - self.startTime))
        if self.pauseTransitions["/state_B"].enabled_event == None:
            pass
    
    def _state_Debug_enter(self):
        self.debugFlag = True
        print("DEBUG MODE")
        print("Current State: ", self.current_state.name)
        print("counter: ", self.counter)
    
    def _state_Debug_exit(self):
        self.cumulativeDebugTime = (self.getSimulatedTime() - self.executionTime)
    
    def continueGuard_state_A(self, parameters):
        return self.current_state == self.states["/state_A"]
    
    def continueGuard_state_A_state_A1(self, parameters):
        return self.current_state == self.states["/state_A/state_A1"]
    
    def continueGuard_state_A_state_A2(self, parameters):
        return self.current_state == self.states["/state_A/state_A2"]
    
    def continueGuard_state_B(self, parameters):
        return self.current_state == self.states["/state_B"]
    
    def initializeStatechart(self):
        # enter default state
        self.default_targets = self.states["/state_A"].getEffectiveTargetStates()
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