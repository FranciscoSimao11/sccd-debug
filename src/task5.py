"""
Generated by Statechart compiler by Glenn De Jonghe, Joeri Exelmans, Simon Van Mierlo, and Yentl Van Tendeloo (for the inspiration)

Model author: Francisco Simoes
Model name:   Task5

"""

from python_sccd.python_sccd_runtime.statecharts_core import *
from sccd.runtime.statecharts_core import *
from python_sccd.python_sccd_runtime.colors import *
import argparse
from sccd.compiler.utils import FileWriter
import os
import inspect
from time import sleep

# package "Task5"

class MainApp(RuntimeClassBase):
    def __init__(self, controller):
        RuntimeClassBase.__init__(self, controller)
        
        self.semantics.big_step_maximality = StatechartSemantics.TakeMany
        self.semantics.internal_event_lifeline = StatechartSemantics.Queue
        self.semantics.input_event_lifeline = StatechartSemantics.FirstComboStep
        self.semantics.priority = StatechartSemantics.SourceParent
        self.semantics.concurrency = StatechartSemantics.Single
        
        self.firstTime = True
        self.didCalcs = Queue()
        self.active_states = Queue()
        self.startTime = 0.0
        self.executionTime = 0.0
        self.localExecutionTime = 0.0
        self.cumulativeDebugTime = 0.0
        self.tracedEvents = []
        self.debugging = False
        self.expiredTimestamps = []
        
        # set execution speed
        self.setSimulationSpeed()
        
        # build Statechart structure
        self.build_statechart_structure()
        
        # user defined attributes
        self.x = 3
        
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
            self.scaleFactor = 1.0
            if args['simType'] == 0:
                print(colors.fg.yellow+"Real-time Simulation")
            elif args['simType'] == 1:
                print(colors.fg.yellow+"Scaled Real-time Simulation")
                if args['factor'] is not None and args['factor'] > 0:
                    self.scaleFactor = args['factor']
            elif args['simType'] == 2:
                print(colors.fg.yellow+"As-fast-as-possible Simulation")
                self.scaleFactor = float('inf')
            else:
                print(colors.fg.yellow+"Invalid simulation type. Defaulting to Real-time Simulation")
                self.scaleFactor = 1.0
            print(colors.fg.yellow+"Scale Factor: {}".format(self.scaleFactor)+colors.reset)
    
    def user_defined_destructor(self):
        pass
    
    
    # user defined method
    def increment(self):
        self.x = self.x + 1
    
    
    # user defined method
    def decrement(self):
        self.x = self.x - 1
    
    
    # user defined method
    def divideBy2(self):
        self.x = self.x / 2
    
    
    # user defined method
    def multiplyBy2(self):
        self.x = self.x * 2
    
    
    # builds Statechart structure
    def build_statechart_structure(self):
        
        # state <root>
        self.states[""] = State(0, "", self)
        
        # state /A
        self.states["/A"] = State(1, "/A", self)
        self.states["/A"].setEnter(self._A_enter)
        self.states["/A"].setExit(self._A_exit)
        
        # state /A/B
        self.states["/A/B"] = State(2, "/A/B", self)
        self.states["/A/B"].setEnter(self._A_B_enter)
        self.states["/A/B"].setExit(self._A_B_exit)
        
        # state /A/C
        self.states["/A/C"] = State(3, "/A/C", self)
        self.states["/A/C"].setEnter(self._A_C_enter)
        self.states["/A/C"].setExit(self._A_C_exit)
        
        # state /D
        self.states["/D"] = State(4, "/D", self)
        self.states["/D"].setEnter(self._D_enter)
        self.states["/D"].setExit(self._D_exit)
        
        # state /state_Debug
        self.states["/state_Debug"] = State(5, "/state_Debug", self)
        self.states["/state_Debug"].setEnter(self._state_Debug_enter)
        self.states["/state_Debug"].setExit(self._state_Debug_exit)
        
        # state /state_Final
        self.states["/state_Final"] = State(6, "/state_Final", self)
        self.states["/state_Final"].setEnter(self._state_Final_enter)
        
        # state /state_Help
        self.states["/state_Help"] = State(7, "/state_Help", self)
        self.states["/state_Help"].setEnter(self._state_Help_enter)
        self.states["/state_Help"].setExit(self._state_Help_exit)
        
        # debug events
        pauseEvent = Event("pause", self.getInPortName("input"))
        stopEvent = Event("stop", self.getInPortName("input"))
        continueEvent = Event("continue", self.getInPortName("input"))
        helpEvent = Event("help", self.getInPortName("input"))
        
        # debug transitions
        self.pauseTransitions = {}
        self.timedTransitions = {}
        self.eventTransitions = {}
        self.createdTransitions = {}
        self.stopTransitions = {}
        self.helpTransitions = {}
        self.timeBreakpointTransitions = {}
        self.genBreakpointTransitions = {}
        
        # add children
        self.states[""].addChild(self.states["/A"])
        self.states[""].addChild(self.states["/D"])
        self.states["/A"].addChild(self.states["/A/B"])
        self.states["/A"].addChild(self.states["/A/C"])
        self.states[""].addChild(self.states["/state_Debug"])
        self.states[""].addChild(self.states["/state_Final"])
        self.states[""].addChild(self.states["/state_Help"])
        self.states[""].fixTree()
        self.states[""].default_state = self.states["/A"]
        self.states["/A"].default_state = self.states["/A/B"]
        
        # transition /A/B
        self.eventTransitions["/A/B"] = []
        self.timedTransitions["/A/B"] = []
        self.createdTransitions["/A/B"] = []
        self.timeBreakpointTransitions["/A/B"] = []
        self.genBreakpointTransitions["/A/B"] = []
        _A_B_0 = Transition(self, self.states["/A/B"], [self.states["/A/B"]])
        _A_B_0.setAction(self._A_B_0_exec)
        _A_B_0.setTrigger(Event("e1", self.getInPortName("input")))
        self.states["/A/B"].addTransition(_A_B_0)
        self.eventTransitions["/A/B"].append(_A_B_0)
        _A_B_1 = Transition(self, self.states["/A/B"], [self.states["/A/C"]])
        _A_B_1.setAction(self._A_B_1_exec)
        _A_B_1.setTrigger(Event("e2", self.getInPortName("input")))
        self.states["/A/B"].addTransition(_A_B_1)
        self.eventTransitions["/A/B"].append(_A_B_1)
        
        # transition /A/C
        self.eventTransitions["/A/C"] = []
        self.timedTransitions["/A/C"] = []
        self.createdTransitions["/A/C"] = []
        self.timeBreakpointTransitions["/A/C"] = []
        self.genBreakpointTransitions["/A/C"] = []
        _A_C_0 = Transition(self, self.states["/A/C"], [self.states["/A/C"]])
        _A_C_0.setAction(self._A_C_0_exec)
        _A_C_0.setTrigger(Event("e4", self.getInPortName("input")))
        self.states["/A/C"].addTransition(_A_C_0)
        self.eventTransitions["/A/C"].append(_A_C_0)
        _A_C_1 = Transition(self, self.states["/A/C"], [self.states["/D"]])
        _A_C_1.setTrigger(Event("e5", self.getInPortName("input")))
        self.states["/A/C"].addTransition(_A_C_1)
        self.eventTransitions["/A/C"].append(_A_C_1)
        _A_C_2 = Transition(self, self.states["/A/C"], [self.states["/A/B"]])
        _A_C_2.setTrigger(Event("e3", self.getInPortName("input")))
        self.states["/A/C"].addTransition(_A_C_2)
        self.eventTransitions["/A/C"].append(_A_C_2)
        
        # transition /D
        self.eventTransitions["/D"] = []
        self.timedTransitions["/D"] = []
        self.createdTransitions["/D"] = []
        self.timeBreakpointTransitions["/D"] = []
        self.genBreakpointTransitions["/D"] = []
        
        # transition /A
        self.eventTransitions["/A"] = []
        self.timedTransitions["/A"] = []
        self.createdTransitions["/A"] = []
        self.timeBreakpointTransitions["/A"] = []
        self.genBreakpointTransitions["/A"] = []
        _A_0 = Transition(self, self.states["/A"], [self.states["/A"]])
        _A_0.setTrigger(Event("e6", self.getInPortName("input")))
        self.states["/A"].addTransition(_A_0)
        self.eventTransitions["/A"].append(_A_0)
        
        # transitions /state_Debug
        # /state_Debug to /state_Help
        state_Debug_to_state_Help = Transition(self, self.states["/state_Debug"], [self.states["/state_Help"]])
        state_Debug_to_state_Help.setTrigger(helpEvent)
        self.states["/state_Debug"].addTransition(state_Debug_to_state_Help)
        
        # /state_Help to /state_Debug
        state_Help_to_state_Debug = Transition(self, self.states["/state_Help"], [self.states["/state_Debug"]])
        state_Help_to_state_Debug.setTrigger(Event("_0after"))
        state_Help_to_state_Debug.setGuard(self.continueGuard_state_Debug)
        self.states["/state_Help"].addTransition(state_Help_to_state_Debug)
        
        # /state_Debug to /state_Final
        state_Debug_to_state_Final = Transition(self, self.states["/state_Debug"], [self.states["/state_Final"]])
        state_Debug_to_state_Final.setTrigger(Event("stop"))
        self.states["/state_Debug"].addTransition(state_Debug_to_state_Final)
        self.debugToFinal = state_Debug_to_state_Final
        
        # _A to /state_Debug
        _A_to_state_Debug = Transition(self, self.states["/A"], [self.states["/state_Debug"]])
        _A_to_state_Debug.setTrigger(pauseEvent)
        self.states["/A"].addTransition(_A_to_state_Debug)
        self.pauseTransitions["/A"] = _A_to_state_Debug
        
        # A from /state_Debug
        _state_Debug_to_A = Transition(self, self.states["/state_Debug"], [self.states["/A"]])
        _state_Debug_to_A.setTrigger(continueEvent)
        _state_Debug_to_A.setGuard(self.continueGuard_A)
        self.states["/state_Debug"].addTransition(_state_Debug_to_A)
        
        # _A to /state_Help
        _A_to_state_Help = Transition(self, self.states["/A"], [self.states["/state_Help"]])
        _A_to_state_Help.setTrigger(helpEvent)
        self.states["/A"].addTransition(_A_to_state_Help)
        self.helpTransitions["/A"] = _A_to_state_Help
        
        # A from /state_Help
        _state_Help_to_A = Transition(self, self.states["/state_Help"], [self.states["/A"]])
        _state_Help_to_A.setTrigger(Event("_0after"))
        _state_Help_to_A.setGuard(self.continueGuard_A)
        self.states["/state_Help"].addTransition(_state_Help_to_A)
        
        # _A to /state_Final
        _A_to_state_Final = Transition(self, self.states["/A"], [self.states["/state_Final"]])
        _A_to_state_Final.setTrigger(stopEvent)
        self.states["/A"].addTransition(_A_to_state_Final)
        self.stopTransitions["/A"] = _A_to_state_Final
        
        # _A_B to /state_Debug
        _A_B_to_state_Debug = Transition(self, self.states["/A/B"], [self.states["/state_Debug"]])
        _A_B_to_state_Debug.setTrigger(pauseEvent)
        self.states["/A/B"].addTransition(_A_B_to_state_Debug)
        self.pauseTransitions["/A/B"] = _A_B_to_state_Debug
        
        # A_B from /state_Debug
        _state_Debug_to_A_B = Transition(self, self.states["/state_Debug"], [self.states["/A/B"]])
        _state_Debug_to_A_B.setTrigger(continueEvent)
        _state_Debug_to_A_B.setGuard(self.continueGuard_A_B)
        self.states["/state_Debug"].addTransition(_state_Debug_to_A_B)
        
        # _A_B to /state_Help
        _A_B_to_state_Help = Transition(self, self.states["/A/B"], [self.states["/state_Help"]])
        _A_B_to_state_Help.setTrigger(helpEvent)
        self.states["/A/B"].addTransition(_A_B_to_state_Help)
        self.helpTransitions["/A/B"] = _A_B_to_state_Help
        
        # A_B from /state_Help
        _state_Help_to_A_B = Transition(self, self.states["/state_Help"], [self.states["/A/B"]])
        _state_Help_to_A_B.setTrigger(Event("_0after"))
        _state_Help_to_A_B.setGuard(self.continueGuard_A_B)
        self.states["/state_Help"].addTransition(_state_Help_to_A_B)
        
        # _A_B to /state_Final
        _A_B_to_state_Final = Transition(self, self.states["/A/B"], [self.states["/state_Final"]])
        _A_B_to_state_Final.setTrigger(stopEvent)
        self.states["/A/B"].addTransition(_A_B_to_state_Final)
        self.stopTransitions["/A/B"] = _A_B_to_state_Final
        
        # _A_C to /state_Debug
        _A_C_to_state_Debug = Transition(self, self.states["/A/C"], [self.states["/state_Debug"]])
        _A_C_to_state_Debug.setTrigger(pauseEvent)
        self.states["/A/C"].addTransition(_A_C_to_state_Debug)
        self.pauseTransitions["/A/C"] = _A_C_to_state_Debug
        
        # A_C from /state_Debug
        _state_Debug_to_A_C = Transition(self, self.states["/state_Debug"], [self.states["/A/C"]])
        _state_Debug_to_A_C.setTrigger(continueEvent)
        _state_Debug_to_A_C.setGuard(self.continueGuard_A_C)
        self.states["/state_Debug"].addTransition(_state_Debug_to_A_C)
        
        # _A_C to /state_Help
        _A_C_to_state_Help = Transition(self, self.states["/A/C"], [self.states["/state_Help"]])
        _A_C_to_state_Help.setTrigger(helpEvent)
        self.states["/A/C"].addTransition(_A_C_to_state_Help)
        self.helpTransitions["/A/C"] = _A_C_to_state_Help
        
        # A_C from /state_Help
        _state_Help_to_A_C = Transition(self, self.states["/state_Help"], [self.states["/A/C"]])
        _state_Help_to_A_C.setTrigger(Event("_0after"))
        _state_Help_to_A_C.setGuard(self.continueGuard_A_C)
        self.states["/state_Help"].addTransition(_state_Help_to_A_C)
        
        # _A_C to /state_Final
        _A_C_to_state_Final = Transition(self, self.states["/A/C"], [self.states["/state_Final"]])
        _A_C_to_state_Final.setTrigger(stopEvent)
        self.states["/A/C"].addTransition(_A_C_to_state_Final)
        self.stopTransitions["/A/C"] = _A_C_to_state_Final
        
        # _D to /state_Debug
        _D_to_state_Debug = Transition(self, self.states["/D"], [self.states["/state_Debug"]])
        _D_to_state_Debug.setTrigger(pauseEvent)
        self.states["/D"].addTransition(_D_to_state_Debug)
        self.pauseTransitions["/D"] = _D_to_state_Debug
        
        # D from /state_Debug
        _state_Debug_to_D = Transition(self, self.states["/state_Debug"], [self.states["/D"]])
        _state_Debug_to_D.setTrigger(continueEvent)
        _state_Debug_to_D.setGuard(self.continueGuard_D)
        self.states["/state_Debug"].addTransition(_state_Debug_to_D)
        
        # _D to /state_Help
        _D_to_state_Help = Transition(self, self.states["/D"], [self.states["/state_Help"]])
        _D_to_state_Help.setTrigger(helpEvent)
        self.states["/D"].addTransition(_D_to_state_Help)
        self.helpTransitions["/D"] = _D_to_state_Help
        
        # D from /state_Help
        _state_Help_to_D = Transition(self, self.states["/state_Help"], [self.states["/D"]])
        _state_Help_to_D.setTrigger(Event("_0after"))
        _state_Help_to_D.setGuard(self.continueGuard_D)
        self.states["/state_Help"].addTransition(_state_Help_to_D)
        
        # _D to /state_Final
        _D_to_state_Final = Transition(self, self.states["/D"], [self.states["/state_Final"]])
        _D_to_state_Final.setTrigger(stopEvent)
        self.states["/D"].addTransition(_D_to_state_Final)
        self.stopTransitions["/D"] = _D_to_state_Final
        
    
    def _A_enter(self):
        self.current_state = self.states["/A"]
        self.debugging = False
        self.startTime = self.getSimulatedTime()
        
        
        if self.firstTime == True:
            self.localExecutionTime = 0.0
            self.increment()
            
            self.print_internal_state("/A")
            event = "entry: /A"
            allAttTuples = []
            allAttTuples.append(["x", self.x])
            self.saveEvent(event, self.getSimulatedTime(), allAttTuples)
            print((colors.fg.lightgreen + "Available Transition Options:") + colors.reset)
            self.process_event_transitions("/A")
            
        else:
            event = "re-entry: /A"
            allAttTuples = []
            allAttTuples.append(["x", self.x])
            self.saveEvent(event, self.getSimulatedTime(), allAttTuples)
    
    def _A_exit(self):
        index = 1
        for et in self.expiredTimestamps:
            self.removeTimer(index)
            index = (index + 1)
        
        found = False
        for b in self.timeBreakpointTransitions["/A"]:
            if b.enabled_event != None:
                found = True
                timerIndex = int(b.enabled_event.name[1:2])
                startingIndex = 2
                self.expiredTimestamps[timerIndex - startingIndex] = True
        
        for b in self.genBreakpointTransitions["/A"]:
            if b.enabled_event != None:
                found = True
        
        if ((self.pauseTransitions["/A"].enabled_event == None) and (not found)) and (self.helpTransitions["/A"].enabled_event == None):
            self.decrement()
            self.firstTime = True
        
        allTransitions = []
        allTransitions.extend(self.timedTransitions["/A"])
        allTransitions.extend(self.eventTransitions["/A"])
        allTransitions.extend(self.timeBreakpointTransitions["/A"])
        allTransitions.extend(self.genBreakpointTransitions["/A"])
        allTransitions.extend(self.createdTransitions["/A"])
        allTransitions.append(self.stopTransitions["/A"])
        allTransitions.append(self.pauseTransitions["/A"])
        allTransitions.append(self.helpTransitions["/A"])
        event = "exit: /A"
        for tr in allTransitions:
            if not (tr.enabled_event == None):
                event = (event + (" - " + tr.enabled_event.name))
        allAttTuples = []
        allAttTuples.append(["x", self.x])
        self.saveEvent(event, self.getSimulatedTime(), allAttTuples)
    
    def _A_B_enter(self):
        self.current_state = self.states["/A/B"]
        self.debugging = False
        self.startTime = self.getSimulatedTime()
        
        while (not self.didCalcs.empty()):
            self.didCalcs.get()
        
        if self.firstTime == True:
            self.localExecutionTime = 0.0
            self.active_states.put(self.current_state)
            
            self.divideBy2()
            
            self.print_internal_state("/A/B")
            event = "entry: /A/B"
            allAttTuples = []
            allAttTuples.append(["x", self.x])
            self.saveEvent(event, self.getSimulatedTime(), allAttTuples)
            print((colors.fg.lightgreen + "Available Transition Options:") + colors.reset)
            self.process_event_transitions("/A/B")
            
            self.print_prompt()
        else:
            event = "re-entry: /A/B"
            allAttTuples = []
            allAttTuples.append(["x", self.x])
            self.saveEvent(event, self.getSimulatedTime(), allAttTuples)
            self.print_prompt()
    
    def _A_B_exit(self):
        index = 1
        for et in self.expiredTimestamps:
            self.removeTimer(index)
            index = (index + 1)
        
        if self.didCalcs.empty():
            self.localExecutionTime = (self.localExecutionTime + (self.getSimulatedTime() - self.startTime))
            self.executionTime = (self.executionTime + (self.getSimulatedTime() - self.startTime))
            self.didCalcs.put(True)
        
        found = False
        for b in self.timeBreakpointTransitions["/A/B"]:
            if b.enabled_event != None:
                found = True
                timerIndex = int(b.enabled_event.name[1:2])
                startingIndex = 2
                self.expiredTimestamps[timerIndex - startingIndex] = True
        
        for b in self.genBreakpointTransitions["/A/B"]:
            if b.enabled_event != None:
                found = True
        
        if ((self.pauseTransitions["/A/B"].enabled_event == None) and (not found)) and (self.helpTransitions["/A/B"].enabled_event == None):
            self.increment()
            self.increment()
            self.increment()
            self.firstTime = True
            queue = self.active_states.queue
            if queue[0] == self.states["/A/B"]:
                self.active_states.get()
            else:
                index = 0
                iteration = 0
                for e in queue:
                    if self.states["/A/B"] == e:
                        index = iteration
                    iteration = (iteration + 1)
                del self.active_states.queue[index]
        
        allTransitions = []
        allTransitions.extend(self.timedTransitions["/A/B"])
        allTransitions.extend(self.eventTransitions["/A/B"])
        allTransitions.extend(self.timeBreakpointTransitions["/A/B"])
        allTransitions.extend(self.genBreakpointTransitions["/A/B"])
        allTransitions.extend(self.createdTransitions["/A/B"])
        allTransitions.append(self.stopTransitions["/A/B"])
        allTransitions.append(self.pauseTransitions["/A/B"])
        allTransitions.append(self.helpTransitions["/A/B"])
        event = "exit: /A/B"
        for tr in allTransitions:
            if not (tr.enabled_event == None):
                event = (event + (" - " + tr.enabled_event.name))
        allAttTuples = []
        allAttTuples.append(["x", self.x])
        self.saveEvent(event, self.getSimulatedTime(), allAttTuples)
    
    def _A_C_enter(self):
        self.current_state = self.states["/A/C"]
        self.debugging = False
        self.startTime = self.getSimulatedTime()
        
        while (not self.didCalcs.empty()):
            self.didCalcs.get()
        
        if self.firstTime == True:
            self.localExecutionTime = 0.0
            self.active_states.put(self.current_state)
            
            
            self.print_internal_state("/A/C")
            event = "entry: /A/C"
            allAttTuples = []
            allAttTuples.append(["x", self.x])
            self.saveEvent(event, self.getSimulatedTime(), allAttTuples)
            print((colors.fg.lightgreen + "Available Transition Options:") + colors.reset)
            self.process_event_transitions("/A/C")
            
            self.print_prompt()
        else:
            event = "re-entry: /A/C"
            allAttTuples = []
            allAttTuples.append(["x", self.x])
            self.saveEvent(event, self.getSimulatedTime(), allAttTuples)
            self.print_prompt()
    
    def _A_C_exit(self):
        index = 1
        for et in self.expiredTimestamps:
            self.removeTimer(index)
            index = (index + 1)
        
        if self.didCalcs.empty():
            self.localExecutionTime = (self.localExecutionTime + (self.getSimulatedTime() - self.startTime))
            self.executionTime = (self.executionTime + (self.getSimulatedTime() - self.startTime))
            self.didCalcs.put(True)
        
        found = False
        for b in self.timeBreakpointTransitions["/A/C"]:
            if b.enabled_event != None:
                found = True
                timerIndex = int(b.enabled_event.name[1:2])
                startingIndex = 2
                self.expiredTimestamps[timerIndex - startingIndex] = True
        
        for b in self.genBreakpointTransitions["/A/C"]:
            if b.enabled_event != None:
                found = True
        
        if ((self.pauseTransitions["/A/C"].enabled_event == None) and (not found)) and (self.helpTransitions["/A/C"].enabled_event == None):
            self.firstTime = True
            queue = self.active_states.queue
            if queue[0] == self.states["/A/C"]:
                self.active_states.get()
            else:
                index = 0
                iteration = 0
                for e in queue:
                    if self.states["/A/C"] == e:
                        index = iteration
                    iteration = (iteration + 1)
                del self.active_states.queue[index]
        
        allTransitions = []
        allTransitions.extend(self.timedTransitions["/A/C"])
        allTransitions.extend(self.eventTransitions["/A/C"])
        allTransitions.extend(self.timeBreakpointTransitions["/A/C"])
        allTransitions.extend(self.genBreakpointTransitions["/A/C"])
        allTransitions.extend(self.createdTransitions["/A/C"])
        allTransitions.append(self.stopTransitions["/A/C"])
        allTransitions.append(self.pauseTransitions["/A/C"])
        allTransitions.append(self.helpTransitions["/A/C"])
        event = "exit: /A/C"
        for tr in allTransitions:
            if not (tr.enabled_event == None):
                event = (event + (" - " + tr.enabled_event.name))
        allAttTuples = []
        allAttTuples.append(["x", self.x])
        self.saveEvent(event, self.getSimulatedTime(), allAttTuples)
    
    def _D_enter(self):
        self.current_state = self.states["/D"]
        self.debugging = False
        self.startTime = self.getSimulatedTime()
        
        while (not self.didCalcs.empty()):
            self.didCalcs.get()
        
        if self.firstTime == True:
            self.localExecutionTime = 0.0
            self.active_states.put(self.current_state)
            
            self.increment()
            
            self.print_internal_state("/D")
            event = "entry: /D"
            allAttTuples = []
            allAttTuples.append(["x", self.x])
            self.saveEvent(event, self.getSimulatedTime(), allAttTuples)
            
            self.print_prompt()
        else:
            event = "re-entry: /D"
            allAttTuples = []
            allAttTuples.append(["x", self.x])
            self.saveEvent(event, self.getSimulatedTime(), allAttTuples)
            self.print_prompt()
    
    def _D_exit(self):
        index = 1
        for et in self.expiredTimestamps:
            self.removeTimer(index)
            index = (index + 1)
        
        if self.didCalcs.empty():
            self.localExecutionTime = (self.localExecutionTime + (self.getSimulatedTime() - self.startTime))
            self.executionTime = (self.executionTime + (self.getSimulatedTime() - self.startTime))
            self.didCalcs.put(True)
        
        found = False
        for b in self.timeBreakpointTransitions["/D"]:
            if b.enabled_event != None:
                found = True
                timerIndex = int(b.enabled_event.name[1:2])
                startingIndex = 2
                self.expiredTimestamps[timerIndex - startingIndex] = True
        
        for b in self.genBreakpointTransitions["/D"]:
            if b.enabled_event != None:
                found = True
        
        if ((self.pauseTransitions["/D"].enabled_event == None) and (not found)) and (self.helpTransitions["/D"].enabled_event == None):
            self.firstTime = True
            queue = self.active_states.queue
            if queue[0] == self.states["/D"]:
                self.active_states.get()
            else:
                index = 0
                iteration = 0
                for e in queue:
                    if self.states["/D"] == e:
                        index = iteration
                    iteration = (iteration + 1)
                del self.active_states.queue[index]
        
        allTransitions = []
        allTransitions.extend(self.timedTransitions["/D"])
        allTransitions.extend(self.eventTransitions["/D"])
        allTransitions.extend(self.timeBreakpointTransitions["/D"])
        allTransitions.extend(self.genBreakpointTransitions["/D"])
        allTransitions.extend(self.createdTransitions["/D"])
        allTransitions.append(self.stopTransitions["/D"])
        allTransitions.append(self.pauseTransitions["/D"])
        allTransitions.append(self.helpTransitions["/D"])
        event = "exit: /D"
        for tr in allTransitions:
            if not (tr.enabled_event == None):
                event = (event + (" - " + tr.enabled_event.name))
        allAttTuples = []
        allAttTuples.append(["x", self.x])
        self.saveEvent(event, self.getSimulatedTime(), allAttTuples)
    
    def _state_Debug_enter(self):
        if self.firstTime:
            self.firstTime = False
        self.debugging = True
        targets = list(self.active_states.queue)
        states_names = [s.name for s in targets]
        
        print(colors.fg.lightred),
        print("DEBUG MODE")
        print("Current States: {}".format(states_names))
        print("x" + ": {}".format(self.x))
        print(colors.reset),
        print(colors.fg.lightgrey +"[/state_Debug] > "+colors.reset),
    
    def _state_Debug_exit(self):
        self.cumulativeDebugTime = (self.getSimulatedTime() - self.executionTime)
        targets = list(self.active_states.queue)
        for t in targets:
            self.pauseTransitions[t.name].enabled_event = None
        if self.debugToFinal.enabled_event != None:
            event = "stop"
            allAttTuples = []
            allAttTuples.append(["x", self.x])
            self.saveEvent(event, self.getSimulatedTime(), allAttTuples)
    
    def _state_Final_enter(self):
        outputName = "executionTrace"
        self.controller.stop()
        self.saveExecutionTrace(outputName)
        exit(1)
    
    def _state_Help_enter(self):
        if self.firstTime:
            self.firstTime = False
        print(colors.fg.yellow + "HELP - Available Commands:")
        print("1. " + colors.fg.orange +"pause" + colors.fg.yellow + " - Pauses the execution.")
        print("2. " + colors.fg.orange +"continue" + colors.fg.yellow + " - Continues the execution if it is paused.")
        print("3. " + colors.fg.orange +"step" + colors.fg.yellow + " - If there exists a time-based transition, this command will skip it.")
        print("4. " + colors.fg.orange +"stop" + colors.fg.yellow + " - Stops the execution completely and saves a trace with information about the simulation.")
        print("5. Possible "+ colors.fg.orange +"events"+ colors.fg.yellow + " to simulate are displayed at the arrival of each state if they are available.")
        print("6. To change the "+ colors.fg.orange + "Simulation Type"  + colors.fg.yellow +" and its " + colors.fg.orange +"Scale Factor" + colors.fg.yellow + ", use the flags " + colors.fg.orange + "-s" + colors.fg.yellow + " and " + colors.fg.orange + "-f" + colors.fg.yellow + ", respectively, when executing the generated file.")
        print("7. The " + colors.fg.orange +  "Simulation Type" + colors.fg.yellow + ", " + colors.fg.orange + "-s" + colors.fg.yellow + " may have the following values: " + colors.fg.orange + "0" + colors.fg.yellow + " = Real-Time Simulation; "+ colors.fg.orange + "1" + colors.fg.yellow + " = Scaled Real-Time Simulation; " + colors.fg.orange + "2" + colors.fg.yellow + " = As-fast-as-possible Simulation.")
        print("8. When using the Scaled Real-Time Simulation, a "+ colors.fg.orange + "Scale Factor" + colors.fg.yellow + ", " + colors.fg.orange + "-f" + colors.fg.yellow + " may be added. Its value may be any number > 0.")
        print("9. To add a " + colors.fg.orange + "breakpoint" + colors.fg.yellow + ", edit the " + colors.fg.orange + "breakpoints.xml" + colors.fg.yellow +" file directly." + colors.reset)
        self.addTimer(0, 0)
    
    
    def _state_Help_exit(self):
        self.removeTimer(0)
        targets = list(self.active_states.queue)
        for t in targets:
            self.helpTransitions[t.name].enabled_event = None
    
    def process_time_transitions(self, timers, state_name):
        iteration = 0
        chosen = None
        lowest = timers[0]
        for t in self.timedTransitions[state_name]:
            if lowest >= timers[iteration]:
                lowest = timers[iteration]
                chosen = t
            iteration = iteration + 1
        if iteration > 0:
            temp = Transition(self, chosen.source, chosen.targets)
            temp.setTrigger(Event("step", self.getInPortName("input")))
            temp.setAction(chosen.action)
            temp.setGuard(chosen.guard)
            if not self.listContains(self.createdTransitions[state_name], temp):
                self.createdTransitions[state_name].append(temp)
                chosen.source.addTransition(temp)
            attrs = [s.name for s in chosen.targets]
            guard = ((inspect.getsourcelines(chosen.guard)[0][1].split('return')[1]).lstrip())[:-1] if chosen.guard != None else chosen.guard
            print((colors.fg.lightgreen + "[time-based]" + colors.fg.lightgrey +" type " + colors.fg.pink +"step" + colors.fg.lightgrey + " to skip the transition to "+ colors.fg.cyan +"{}" + colors.fg.lightgrey +" which has a duration of " + colors.fg.pink + "{}" + colors.fg.lightgrey +" seconds and the guard condition " + colors.fg.pink + "{}" + colors.reset).format(attrs, lowest, guard))
    
    def process_event_transitions(self, state_name):
        possibleT = self.eventTransitions[state_name]
        for t in possibleT:
            attrs = [s.name for s in t.targets]
            guard = ((inspect.getsourcelines(t.guard)[0][1].split('return')[1]).lstrip())[:-1] if t.guard != None else t.guard
            print((colors.fg.lightgreen + "[event-based]"  + colors.fg.lightgrey +" type " + colors.fg.pink +"{}"+ colors.fg.lightgrey + " to perform the transition to "+ colors.fg.cyan + "{}" + colors.fg.lightgrey + " with the guard condition " + colors.fg.pink + "{}"+ colors.reset).format(t.trigger.name, attrs, guard))
    
    def print_internal_state(self, state_name):
        print("\n" + ((colors.fg.lightgrey + "Entered ") + (colors.fg.cyan + state_name)))
        print(colors.fg.cyan + "x" + (": {}" + colors.reset).format(self.x))
    
    def print_prompt(self):
        print(colors.fg.lightgrey +"["),
        size = len(self.active_states.queue)
        iteration = 0
        for s in list(self.active_states.queue):
            print(s.name),
            if iteration < (size - 1):
                print(", "),
            iteration = (iteration + 1)
        print("] > "+colors.reset),
    
    def saveExecutionTrace(self, outputName):
        currDir = os.getcwd()
        flag = False
        biggestSize = 0
        for entry in os.listdir(currDir):
            if os.path.isfile(os.path.join(currDir, entry)) and (outputName) in entry and len(entry) > biggestSize:
                outputName = entry[:-4] + "_1" + ".txt"
                flag = True
                biggestSize = len(entry)
                
        if not flag:
            outputName = outputName + ".txt"
        
        simTime = "Total Simulation Time: " + str(float(self.getSimulatedTime())) + " ms (includes Debug Time)"
        exTime = "Execution Time: " + str(self.executionTime) + " ms"
        debugTime = "Total Debug Time: " + str(self.cumulativeDebugTime) + " ms"
        
        f = FileWriter(outputName)
        f.write("Execution Info")
        f.write("")
        f.write(simTime)
        f.write(exTime)
        f.write(debugTime)
        f.write("")
        f.write("Events")
        for ide, event in enumerate(self.tracedEvents):
            eventName = event.getEventName()
            timestamp = event.getTimestamp()
            attributeValues = ""
            for v in event.getAttributeValues():
                attributeValues += v[0] + ": " + str(v[1]) + "; "
            eventInfo = str(ide) + ". Timestamp: " + str(timestamp) +  "; Name: " + eventName + ";  Attributes: ["  + attributeValues + "]"
            # print(ide)
            # print(eventName)
            f.write(eventInfo)
        f.close() 
    
    def saveEvent(self, event_name, timestamp, attribute_values):
        self.tracedEvents.append(TracedEvent(event_name, timestamp, attribute_values))
    
    def listContains(self, transitions, newTransition):
        flag = False
        for t in transitions:
            if ((((t.source == newTransition.source) and (t.targets == newTransition.targets)) and (t.trigger.name == newTransition.trigger.name)) and (t.trigger.port == newTransition.trigger.port)) and (t.action == newTransition.action):
                flag = True
        return flag
    
    def _A_B_0_exec(self, parameters):
        self.decrement()
    
    def _A_B_1_exec(self, parameters):
        self.multiplyBy2()
    
    def _A_C_0_exec(self, parameters):
        self.increment()
    
    def continueGuard_state_Debug(self, parameters):
        return self.debugging
    
    def continueGuard_A(self, parameters):
        return list(self.active_states.queue) == list([self.states["/A"]])
    
    def continueGuard_A_B(self, parameters):
        return list(self.active_states.queue) == list([self.states["/A/B"]])
    
    def continueGuard_A_C(self, parameters):
        return list(self.active_states.queue) == list([self.states["/A/C"]])
    
    def continueGuard_D(self, parameters):
        return list(self.active_states.queue) == list([self.states["/D"]])
    
    def initializeStatechart(self):
        # enter default state
        print(colors.fg.yellow + "Type " + colors.fg.orange + "help" + colors.fg.yellow + " to see the available commands." + colors.reset)
        event = "start"
        allAttTuples = []
        allAttTuples.append(["x", self.x])
        self.saveEvent(event, self.getSimulatedTime(), allAttTuples)
        self.default_targets = self.states["/A"].getEffectiveTargetStates()
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