"""
Generated by Statechart compiler by Glenn De Jonghe, Joeri Exelmans, Simon Van Mierlo, and Yentl Van Tendeloo (for the inspiration)

Model author: Francisco Simoes
Model name:   Counter

"""

from time import sleep
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
        self.timeDiff = 0
        self.executionTime = 0.0 #excluding debug time
        self.localExecutionTime = 0.0 #execution time for a particular state
        self.cumulativeDebugTime = 0

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
        
        # state /state_B
        self.states["/state_B"] = State(2, "/state_B", self)
        self.states["/state_B"].setEnter(self._state_B_enter)
        self.states["/state_B"].setExit(self._state_B_exit)
        
        # state /state_C
        self.states["/state_C"] = State(3, "/state_C", self)
        self.states["/state_C"].setEnter(self._state_C_enter)
        self.states["/state_C"].setExit(self._state_C_exit)
        
        # state /state_D
        self.states["/state_D"] = State(4, "/state_D", self)
        self.states["/state_D"].setEnter(self._state_D_enter)
        self.states["/state_D"].setExit(self._state_D_exit)
        
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
        self.states[""].addChild(self.states["/state_C"])
        self.states[""].addChild(self.states["/state_D"])
        self.states[""].addChild(self.states["/state_Debug"])
        self.states[""].fixTree()
        self.states[""].default_state = self.states["/state_A"]
        
        # transition /state_A
        self.eventTransitions["/state_A"] = []
        _state_A_0 = Transition(self, self.states["/state_A"], [self.states["/state_B"]])
        _state_A_0.setTrigger(Event("_0after"))
        self.states["/state_A"].addTransition(_state_A_0)
        self.timedTransitions.append(_state_A_0)
        _state_A_1 = Transition(self, self.states["/state_A"], [self.states["/state_C"]])
        _state_A_1.setTrigger(Event("_1after"))
        self.states["/state_A"].addTransition(_state_A_1)
        self.timedTransitions.append(_state_A_1)
        _state_A_2 = Transition(self, self.states["/state_A"], [self.states["/state_D"]])
        _state_A_2.setTrigger(Event("d", self.getInPortName("input")))
        self.states["/state_A"].addTransition(_state_A_2)
        self.eventTransitions["/state_A"].append(_state_A_2)
        
        # transition /state_B
        self.eventTransitions["/state_B"] = []
        _state_B_0 = Transition(self, self.states["/state_B"], [self.states["/state_A"]])
        _state_B_0.setTrigger(Event("move", self.getInPortName("input")))
        self.states["/state_B"].addTransition(_state_B_0)
        self.eventTransitions["/state_B"].append(_state_B_0)
        
        # transition /state_C
        self.eventTransitions["/state_C"] = []
        _state_C_0 = Transition(self, self.states["/state_C"], [self.states["/state_A"]])
        _state_C_0.setTrigger(Event("move", self.getInPortName("input")))
        self.states["/state_C"].addTransition(_state_C_0)
        self.eventTransitions["/state_C"].append(_state_C_0)
        
        # transition /state_D
        self.eventTransitions["/state_D"] = []
        _state_D_0 = Transition(self, self.states["/state_D"], [self.states["/state_A"]])
        _state_D_0.setTrigger(Event("move", self.getInPortName("input")))
        self.states["/state_D"].addTransition(_state_D_0)
        self.eventTransitions["/state_D"].append(_state_D_0)
        
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
        
        # _state_C to /state_Debug
        _state_C_to_state_Debug = Transition(self, self.states["/state_C"], [self.states["/state_Debug"]])
        _state_C_to_state_Debug.setTrigger(pauseEvent)
        self.states["/state_C"].addTransition(_state_C_to_state_Debug)
        self.pauseTransitions["/state_C"] = _state_C_to_state_Debug
        
        # state_C from /state_Debug
        _state_Debug_to_state_C = Transition(self, self.states["/state_Debug"], [self.states["/state_C"]])
        _state_Debug_to_state_C.setTrigger(continueEvent)
        _state_Debug_to_state_C.setGuard(self.continueGuard_state_C)
        self.states["/state_Debug"].addTransition(_state_Debug_to_state_C)
        
        # _state_D to /state_Debug
        _state_D_to_state_Debug = Transition(self, self.states["/state_D"], [self.states["/state_Debug"]])
        _state_D_to_state_Debug.setTrigger(pauseEvent)
        self.states["/state_D"].addTransition(_state_D_to_state_Debug)
        self.pauseTransitions["/state_D"] = _state_D_to_state_Debug
        
        # state_D from /state_Debug
        _state_Debug_to_state_D = Transition(self, self.states["/state_Debug"], [self.states["/state_D"]])
        _state_Debug_to_state_D.setTrigger(continueEvent)
        _state_Debug_to_state_D.setGuard(self.continueGuard_state_D)
        self.states["/state_Debug"].addTransition(_state_Debug_to_state_D)
        
        breakpoint0 = Transition(self, self.states["/state_B"], [self.states["/state_Debug"]])
        breakpoint0.setTrigger(Event("_2after"))
        self.states["/state_B"].addTransition(breakpoint0)
        
        varBreakpoint0 = Transition(self, self.states["/state_A"], [self.states["/state_Debug"]])
        varBreakpoint0.setTrigger(Event("_3after"))
        self.states["/state_A"].addTransition(varBreakpoint0)
        
        varBreakpoint1 = Transition(self, self.states["/state_B"], [self.states["/state_Debug"]])
        varBreakpoint1.setTrigger(Event("_3after"))
        self.states["/state_B"].addTransition(varBreakpoint1)
        
        varBreakpoint2 = Transition(self, self.states["/state_C"], [self.states["/state_Debug"]])
        varBreakpoint2.setTrigger(Event("_3after"))
        self.states["/state_C"].addTransition(varBreakpoint2)
        
        varBreakpoint3 = Transition(self, self.states["/state_D"], [self.states["/state_Debug"]])
        varBreakpoint3.setTrigger(Event("_3after"))
        self.states["/state_D"].addTransition(varBreakpoint3)
        
    
    def _state_A_enter(self):
        self.current_state = self.states["/state_A"]
        self.current_states.put(self.current_state)
        self.startTime = self.getSimulatedTime()

        if self.debugFlag == False:
            self.localExecutionTime = 0
            self.increment_counter();
            timers = []
            self.addTimer(0, 10 / self.scaleFactor)
            timers.append(10)
            self.addTimer(1, 20 / self.scaleFactor)
            timers.append(20)
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
            
            possibleT = self.eventTransitions["/state_A"]
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
                self.addTimer(3, 0)

            # while True:
            #     print(self.getSimulatedTime())
            #     sleep(1)
        else:
            if self.states["/state_A"].children == []:
                self.debugFlag = False
            print("time left: ", 10.0 - float((self.localExecutionTime/1000.0)))
            self.addTimer(0, 10.0 - (float((self.localExecutionTime/1000.0)) / self.scaleFactor))
            self.addTimer(1, 20 - ((self.localExecutionTime/1000) / self.scaleFactor))
    
    def _state_A_exit(self):
        self.removeTimer(0)
        self.removeTimer(1)
        print("sim: ", self.getSimulatedTime())
        print("start: ", self.startTime)
        #print("diff: ", self.timeDiff*1000)
        #self.executionTime = self.executionTime + (self.getSimulatedTime() - (self.startTime-self.timeDiff*1000))
        self.localExecutionTime = self.localExecutionTime + (self.getSimulatedTime() - self.startTime)
        self.executionTime = self.executionTime + (self.getSimulatedTime() - self.startTime)
        print("local ex: ", self.localExecutionTime)
        #self.localExecutionTime = self.getSimulatedTime() - self.startTime
        #self.executionTime = self.getSimulatedTime() - self.cumulativeDebugTime
        print("ex: ", self.executionTime)
        if self.pauseTransitions["/state_A"].enabled_event == None:
            self.current_states.get()
    
    def _state_B_enter(self):
        self.current_state = self.states["/state_B"]
        self.current_states.put(self.current_state)
        self.startTime = self.getSimulatedTime()

        if self.debugFlag == False:
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
            self.addTimer(2, 0)
            if self.counter == 5:
                self.addTimer(3, 0)
            # while True:
            #     print(self.getSimulatedTime())
        else:
            if self.states["/state_B"].children == []:
                self.debugFlag = False
    
    def _state_B_exit(self):
        self.executionTime = self.executionTime + (self.getSimulatedTime() - (self.startTime-self.timeDiff*1000))
        print("ex: ", self.executionTime)
        if self.pauseTransitions["/state_B"].enabled_event == None:
            self.current_states.get()
    
    def _state_C_enter(self):
        self.current_state = self.states["/state_C"]
        self.current_states.put(self.current_state)
        self.startTime = self.getSimulatedTime()
        
        if self.debugFlag == False:
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
                self.addTimer(3, 0)
        else:
            if self.states["/state_C"].children == []:
                self.debugFlag = False
    
    def _state_C_exit(self):
        if self.pauseTransitions["/state_C"].enabled_event == None:
            self.current_states.get()
    
    def _state_D_enter(self):
        self.current_state = self.states["/state_D"]
        self.current_states.put(self.current_state)
        self.startTime = self.getSimulatedTime()
        
        if self.debugFlag == False:
            self.increment_counter();
            timers = []
            
            possibleT = self.eventTransitions["/state_D"]
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
                self.addTimer(3, 0)
        else:
            if self.states["/state_D"].children == []:
                self.debugFlag = False
    
    def _state_D_exit(self):
        if self.pauseTransitions["/state_D"].enabled_event == None:
            self.current_states.get()
    
    def _state_Debug_enter(self):
        #print(self.getSimulatedTime())
        #self.timeDiff = ((self.getSimulatedTime() - self.startTime) / 1000.0)
        #print("diff debug: ", self.timeDiff)
        self.debugFlag = True
        #self.executionTime = self.executionTime + self.timeDiff
        #print(self.executionTime)
        print("DEBUG MODE")
        print("Current State: ", self.current_state.name)
        print("counter: ", self.counter)
    
    def _state_Debug_exit(self):
        self.cumulativeDebugTime = self.getSimulatedTime() - self.executionTime
        print("cum: ", self.cumulativeDebugTime)

    def continueGuard_state_A(self, parameters):
        return self.current_state == self.states["/state_A"]
    
    def continueGuard_state_B(self, parameters):
        return self.current_state == self.states["/state_B"]
    
    def continueGuard_state_C(self, parameters):
        return self.current_state == self.states["/state_C"]
    
    def continueGuard_state_D(self, parameters):
        return self.current_state == self.states["/state_D"]
    
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