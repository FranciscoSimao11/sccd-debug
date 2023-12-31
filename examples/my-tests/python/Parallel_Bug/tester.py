"""
Generated by Statechart compiler by Glenn De Jonghe, Joeri Exelmans, Simon Van Mierlo, and Yentl Van Tendeloo (for the inspiration)

Date:   Fri Sep 08 11:03:01 2017

Model author: Yentl Van Tendeloo
Model name:   Testing
Model description:
Testing
"""

from sccd.runtime.statecharts_core import *

# package "Testing"

class Testing(RuntimeClassBase):
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
        Testing.user_defined_constructor(self)
    
    def user_defined_constructor(self):
        pass
    
    def user_defined_destructor(self):
        pass
    
    
    # builds Statechart structure
    def build_statechart_structure(self):
        
        # state <root>
        self.states[""] = State(0, "", self)
        
        # state /A
        self.states["/A"] = ParallelState(1, "/A", self)
        
        # state /A/B
        self.states["/A/B"] = State(2, "/A/B", self)
        self.states["/A/B"].setExit(self._A_B_exit)
        
        # state /A/B/1
        self.states["/A/B/1"] = State(3, "/A/B/1", self)
        self.states["/A/B/1"].setEnter(self._A_B_1_enter)
        
        # state /A/D
        self.states["/A/D"] = State(4, "/A/D", self)
        
        # state /A/D/a
        self.states["/A/D/a"] = State(5, "/A/D/a", self)
        
        # state /A/D/b
        self.states["/A/D/b"] = State(6, "/A/D/b", self)
        
        # add children
        self.states[""].addChild(self.states["/A"])
        self.states["/A"].addChild(self.states["/A/B"])
        self.states["/A"].addChild(self.states["/A/D"])
        self.states["/A/B"].addChild(self.states["/A/B/1"])
        self.states["/A/D"].addChild(self.states["/A/D/a"])
        self.states["/A/D"].addChild(self.states["/A/D/b"])
        self.states[""].fixTree()
        self.states[""].default_state = self.states["/A"]
        self.states["/A/B"].default_state = self.states["/A/B/1"]
        self.states["/A/D"].default_state = self.states["/A/D/a"]
        
        # transition /A/D
        _A_D_0 = Transition(self, self.states["/A/D"], [self.states["/A/D/a"]])
        _A_D_0.setTrigger(Event("Z", None))
        self.states["/A/D"].addTransition(_A_D_0)
    
    def _A_B_exit(self):
        raise Exception("Should never leave!")
    
    def _A_B_1_enter(self):
        self.raiseInternalEvent(Event("Z", None, []))
    
    def initializeStatechart(self):
        # enter default state
        self.default_targets = self.states["/A"].getEffectiveTargetStates()
        RuntimeClassBase.initializeStatechart(self)

class ObjectManager(ObjectManagerBase):
    def __init__(self, controller):
        ObjectManagerBase.__init__(self, controller)
    
    def instantiate(self, class_name, construct_params):
        if class_name == "Testing":
            instance = Testing(self.controller)
            instance.associations = {}
        else:
            raise Exception("Cannot instantiate class " + class_name)
        return instance

class Controller(ThreadsControllerBase):
    def __init__(self, keep_running = None, behind_schedule_callback = None):
        if keep_running == None: keep_running = True
        if behind_schedule_callback == None: behind_schedule_callback = None
        ThreadsControllerBase.__init__(self, ObjectManager(self), keep_running, behind_schedule_callback)
        self.object_manager.createInstance("Testing", [])