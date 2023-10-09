"""
Generated by Statechart compiler by Glenn De Jonghe, Joeri Exelmans, Simon Van Mierlo, and Yentl Van Tendeloo (for the inspiration)

Model author: Francisco Simoes
Model name:   Counter

"""

from sccd.runtime.statecharts_core import *
from sccd.runtime.libs.ui import ui
import sccd.runtime.accurate_time

# package "Counter"

class MainApp(RuntimeClassBase):
    def __init__(self, controller):
        RuntimeClassBase.__init__(self, controller)
        
        
        self.semantics.big_step_maximality = StatechartSemantics.TakeMany
        self.semantics.internal_event_lifeline = StatechartSemantics.Queue
        self.semantics.input_event_lifeline = StatechartSemantics.FirstComboStep
        self.semantics.priority = StatechartSemantics.SourceParent
        self.semantics.concurrency = StatechartSemantics.Single
        
        # build Statechart structure
        self.build_statechart_structure()
        
        # call user defined constructor
        MainApp.user_defined_constructor(self)
    
    def user_defined_constructor(self):
        self.counter = 0
    
    def user_defined_destructor(self):
        pass
    
    
    # user defined method
    def increment_counter(self):
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
        
        # add children
        self.states[""].addChild(self.states["/state_A"])
        self.states[""].addChild(self.states["/state_B"])
        self.states[""].fixTree()
        self.states[""].default_state = self.states["/state_A"]
        
        # transition /state_A
        _state_A_0 = Transition(self, self.states["/state_A"], [self.states["/state_B"]])
        _state_A_0.setTrigger(Event("_0after"))
        self.states["/state_A"].addTransition(_state_A_0)
        
        # transition /state_B
        _state_B_0 = Transition(self, self.states["/state_B"], [self.states["/state_A"]])
        _state_B_0.setTrigger(Event("move", self.getInPortName("input")))
        self.states["/state_B"].addTransition(_state_B_0)
    
    def _state_A_enter(self):
        self.increment_counter();
        self.addTimer(0, 10)
    
    def _state_A_exit(self):
        self.removeTimer(0)
    
    def _state_B_enter(self):
        self.increment_counter();
    
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