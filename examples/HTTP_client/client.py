"""
Generated by Statechart compiler by Glenn De Jonghe, Joeri Exelmans, Simon Van Mierlo, and Yentl Van Tendeloo (for the inspiration)

Date:   Wed Aug 17 13:32:50 2016

Model author: Yentl Van Tendeloo
Model name:   HTTP client
Model description:
HTTP client in SCCD
"""

from sccd.runtime.statecharts_core import *
import time
import os
import urllib
import sys
import json

# package "HTTP client"

class Prompt(RuntimeClassBase):
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
        Prompt.user_defined_constructor(self)
    
    def user_defined_constructor(self):
        self.counter = 0
    
    def user_defined_destructor(self):
        pass
    
    
    # builds Statechart structure
    def build_statechart_structure(self):
        
        # state <root>
        self.states[""] = State(0, self)
        
        # state /init
        self.states["/init"] = State(1, self)
        self.states["/init"].setEnter(self._init_enter)
        
        # state /initializing
        self.states["/initializing"] = State(2, self)
        self.states["/initializing"].setEnter(self._initializing_enter)
        self.states["/initializing"].setExit(self._initializing_exit)
        
        # state /send_request
        self.states["/send_request"] = State(3, self)
        self.states["/send_request"].setEnter(self._send_request_enter)
        self.states["/send_request"].setExit(self._send_request_exit)
        
        # state /wait_reply
        self.states["/wait_reply"] = State(4, self)
        self.states["/wait_reply"].setEnter(self._wait_reply_enter)
        self.states["/wait_reply"].setExit(self._wait_reply_exit)
        
        # add children
        self.states[""].addChild(self.states["/init"])
        self.states[""].addChild(self.states["/initializing"])
        self.states[""].addChild(self.states["/send_request"])
        self.states[""].addChild(self.states["/wait_reply"])
        self.states[""].fixTree()
        self.states[""].default_state = self.states["/init"]
        
        # transition /init
        _init_0 = Transition(self, self.states["/init"], [self.states["/initializing"]])
        _init_0.setAction(self._init_0_exec)
        _init_0.setTrigger(Event("instance_created", None))
        self.states["/init"].addTransition(_init_0)
        
        # transition /initializing
        _initializing_0 = Transition(self, self.states["/initializing"], [self.states["/initializing"]])
        _initializing_0.setTrigger(Event("_0after"))
        self.states["/initializing"].addTransition(_initializing_0)
        _initializing_1 = Transition(self, self.states["/initializing"], [self.states["/send_request"]])
        _initializing_1.setTrigger(Event("http_client_ready", None))
        self.states["/initializing"].addTransition(_initializing_1)
        
        # transition /send_request
        _send_request_0 = Transition(self, self.states["/send_request"], [self.states["/wait_reply"]])
        _send_request_0.setAction(self._send_request_0_exec)
        _send_request_0.setTrigger(Event("_1after"))
        self.states["/send_request"].addTransition(_send_request_0)
        
        # transition /wait_reply
        _wait_reply_0 = Transition(self, self.states["/wait_reply"], [self.states["/wait_reply"]])
        _wait_reply_0.setTrigger(Event("_2after"))
        self.states["/wait_reply"].addTransition(_wait_reply_0)
        _wait_reply_1 = Transition(self, self.states["/wait_reply"], [self.states["/send_request"]])
        _wait_reply_1.setAction(self._wait_reply_1_exec)
        _wait_reply_1.setTrigger(Event("HTTP_output", None))
        self.states["/wait_reply"].addTransition(_wait_reply_1)
    
    def _init_enter(self):
        self.big_step.outputEventOM(Event("create_instance", None, [self, 'to_server', 'HTTPClient', '127.0.0.1', 8080]))
    
    def _initializing_enter(self):
        self.addTimer(0, 1.0)
    
    def _initializing_exit(self):
        self.removeTimer(0)
    
    def _send_request_enter(self):
        self.addTimer(1, 1)
    
    def _send_request_exit(self):
        self.removeTimer(1)
    
    def _wait_reply_enter(self):
        self.addTimer(2, 1.0)
    
    def _wait_reply_exit(self):
        self.removeTimer(2)
    
    def _init_0_exec(self, parameters):
        instancename = parameters[0]
        self.big_step.outputEventOM(Event("start_instance", None, [self, instancename]))
    
    def _send_request_0_exec(self, parameters):
        self.big_step.outputEventOM(Event("narrow_cast", None, [self, 'to_server', Event("HTTP_input", None, [str(self.counter), 'parent'])]))
        print("Sending request: %s" % self.counter)
        self.counter += 1
    
    def _wait_reply_1_exec(self, parameters):
        data = parameters[0]
        print("Got response: %s" % data)
    
    def initializeStatechart(self):
        # enter default state
        self.default_targets = self.states["/init"].getEffectiveTargetStates()
        RuntimeClassBase.initializeStatechart(self)

class HTTPClient(RuntimeClassBase):
    def __init__(self, controller, hostname, port):
        RuntimeClassBase.__init__(self, controller)
        
        self.semantics.big_step_maximality = StatechartSemantics.TakeMany
        self.semantics.internal_event_lifeline = StatechartSemantics.Queue
        self.semantics.input_event_lifeline = StatechartSemantics.FirstComboStep
        self.semantics.priority = StatechartSemantics.SourceParent
        self.semantics.concurrency = StatechartSemantics.Single
        
        # build Statechart structure
        self.build_statechart_structure()
        
        # call user defined constructor
        HTTPClient.user_defined_constructor(self, hostname, port)
    
    def user_defined_constructor(self, hostname, port):
        self.socket = None
        self.destination = (hostname, port)
        self.received_data = ""
        self.send_data = ""
        self.queue = []
        self.destinations = []
    
    def user_defined_destructor(self):
        pass
    
    
    # builds Statechart structure
    def build_statechart_structure(self):
        
        # state <root>
        self.states[""] = State(0, self)
        
        # state /init
        self.states["/init"] = State(1, self)
        self.states["/init"].setEnter(self._init_enter)
        
        # state /connecting
        self.states["/connecting"] = State(2, self)
        self.states["/connecting"].setEnter(self._connecting_enter)
        
        # state /connected
        self.states["/connected"] = ParallelState(3, self)
        
        # state /connected/listening
        self.states["/connected/listening"] = State(4, self)
        
        # state /connected/listening/listen
        self.states["/connected/listening/listen"] = State(5, self)
        self.states["/connected/listening/listen"].setEnter(self._connected_listening_listen_enter)
        
        # state /connected/listening/close
        self.states["/connected/listening/close"] = State(6, self)
        
        # state /connected/sending
        self.states["/connected/sending"] = State(7, self)
        
        # state /connected/sending/waiting_for_data
        self.states["/connected/sending/waiting_for_data"] = State(8, self)
        
        # state /connected/sending/transferring
        self.states["/connected/sending/transferring"] = State(9, self)
        
        # state /connected/queueing
        self.states["/connected/queueing"] = State(10, self)
        
        # state /connected/queueing/queueing
        self.states["/connected/queueing/queueing"] = State(11, self)
        self.states["/connected/queueing/queueing"].setEnter(self._connected_queueing_queueing_enter)
        
        # state /connected/parsing
        self.states["/connected/parsing"] = State(12, self)
        
        # state /connected/parsing/wait_for_header
        self.states["/connected/parsing/wait_for_header"] = State(13, self)
        
        # state /connected/parsing/wait_for_payload
        self.states["/connected/parsing/wait_for_payload"] = State(14, self)
        
        # add children
        self.states[""].addChild(self.states["/init"])
        self.states[""].addChild(self.states["/connecting"])
        self.states[""].addChild(self.states["/connected"])
        self.states["/connected"].addChild(self.states["/connected/listening"])
        self.states["/connected"].addChild(self.states["/connected/sending"])
        self.states["/connected"].addChild(self.states["/connected/queueing"])
        self.states["/connected"].addChild(self.states["/connected/parsing"])
        self.states["/connected/listening"].addChild(self.states["/connected/listening/listen"])
        self.states["/connected/listening"].addChild(self.states["/connected/listening/close"])
        self.states["/connected/sending"].addChild(self.states["/connected/sending/waiting_for_data"])
        self.states["/connected/sending"].addChild(self.states["/connected/sending/transferring"])
        self.states["/connected/queueing"].addChild(self.states["/connected/queueing/queueing"])
        self.states["/connected/parsing"].addChild(self.states["/connected/parsing/wait_for_header"])
        self.states["/connected/parsing"].addChild(self.states["/connected/parsing/wait_for_payload"])
        self.states[""].fixTree()
        self.states[""].default_state = self.states["/init"]
        self.states["/connected/listening"].default_state = self.states["/connected/listening/listen"]
        self.states["/connected/sending"].default_state = self.states["/connected/sending/waiting_for_data"]
        self.states["/connected/queueing"].default_state = self.states["/connected/queueing/queueing"]
        self.states["/connected/parsing"].default_state = self.states["/connected/parsing/wait_for_header"]
        
        # transition /init
        _init_0 = Transition(self, self.states["/init"], [self.states["/connecting"]])
        _init_0.setAction(self._init_0_exec)
        _init_0.setTrigger(Event("created_socket", "socket_in"))
        self.states["/init"].addTransition(_init_0)
        
        # transition /connecting
        _connecting_0 = Transition(self, self.states["/connecting"], [self.states["/connected"]])
        _connecting_0.setAction(self._connecting_0_exec)
        _connecting_0.setTrigger(Event("connected_socket", "socket_in"))
        _connecting_0.setGuard(self._connecting_0_guard)
        self.states["/connecting"].addTransition(_connecting_0)
        
        # transition /connected/listening/listen
        _connected_listening_listen_0 = Transition(self, self.states["/connected/listening/listen"], [self.states["/connected/listening/listen"]])
        _connected_listening_listen_0.setAction(self._connected_listening_listen_0_exec)
        _connected_listening_listen_0.setTrigger(Event("received_socket", "socket_in"))
        _connected_listening_listen_0.setGuard(self._connected_listening_listen_0_guard)
        self.states["/connected/listening/listen"].addTransition(_connected_listening_listen_0)
        _connected_listening_listen_1 = Transition(self, self.states["/connected/listening/listen"], [self.states["/connected/listening/close"]])
        _connected_listening_listen_1.setTrigger(Event("received_socket", "socket_in"))
        _connected_listening_listen_1.setGuard(self._connected_listening_listen_1_guard)
        self.states["/connected/listening/listen"].addTransition(_connected_listening_listen_1)
        
        # transition /connected/sending/waiting_for_data
        _connected_sending_waiting_for_data_0 = Transition(self, self.states["/connected/sending/waiting_for_data"], [self.states["/connected/sending/transferring"]])
        _connected_sending_waiting_for_data_0.setAction(self._connected_sending_waiting_for_data_0_exec)
        _connected_sending_waiting_for_data_0.setTrigger(None)
        _connected_sending_waiting_for_data_0.setGuard(self._connected_sending_waiting_for_data_0_guard)
        self.states["/connected/sending/waiting_for_data"].addTransition(_connected_sending_waiting_for_data_0)
        
        # transition /connected/sending/transferring
        _connected_sending_transferring_0 = Transition(self, self.states["/connected/sending/transferring"], [self.states["/connected/sending/waiting_for_data"]])
        _connected_sending_transferring_0.setAction(self._connected_sending_transferring_0_exec)
        _connected_sending_transferring_0.setTrigger(Event("sent_socket", "socket_in"))
        _connected_sending_transferring_0.setGuard(self._connected_sending_transferring_0_guard)
        self.states["/connected/sending/transferring"].addTransition(_connected_sending_transferring_0)
        
        # transition /connected/queueing/queueing
        _connected_queueing_queueing_0 = Transition(self, self.states["/connected/queueing/queueing"], [self.states["/connected/queueing/queueing"]])
        _connected_queueing_queueing_0.setAction(self._connected_queueing_queueing_0_exec)
        _connected_queueing_queueing_0.setTrigger(Event("HTTP_input", None))
        self.states["/connected/queueing/queueing"].addTransition(_connected_queueing_queueing_0)
        
        # transition /connected/parsing/wait_for_header
        _connected_parsing_wait_for_header_0 = Transition(self, self.states["/connected/parsing/wait_for_header"], [self.states["/connected/parsing/wait_for_payload"]])
        _connected_parsing_wait_for_header_0.setAction(self._connected_parsing_wait_for_header_0_exec)
        _connected_parsing_wait_for_header_0.setTrigger(None)
        _connected_parsing_wait_for_header_0.setGuard(self._connected_parsing_wait_for_header_0_guard)
        self.states["/connected/parsing/wait_for_header"].addTransition(_connected_parsing_wait_for_header_0)
        
        # transition /connected/parsing/wait_for_payload
        _connected_parsing_wait_for_payload_0 = Transition(self, self.states["/connected/parsing/wait_for_payload"], [self.states["/connected/parsing/wait_for_header"]])
        _connected_parsing_wait_for_payload_0.setAction(self._connected_parsing_wait_for_payload_0_exec)
        _connected_parsing_wait_for_payload_0.setTrigger(None)
        _connected_parsing_wait_for_payload_0.setGuard(self._connected_parsing_wait_for_payload_0_guard)
        self.states["/connected/parsing/wait_for_payload"].addTransition(_connected_parsing_wait_for_payload_0)
    
    def _init_enter(self):
        self.big_step.outputEvent(Event("create_socket", "", []))
    
    def _connecting_enter(self):
        self.big_step.outputEvent(Event("connect_socket", "", [self.socket, self.destination]))
    
    def _connected_listening_listen_enter(self):
        self.big_step.outputEvent(Event("recv_socket", "socket_out", [self.socket]))
    
    def _connected_queueing_queueing_enter(self):
        pass
    
    def _init_0_exec(self, parameters):
        socket = parameters[0]
        self.socket = socket
    
    def _connecting_0_exec(self, parameters):
        socket = parameters[0]
        self.big_step.outputEventOM(Event("broad_cast", None, [Event("http_client_ready", None, [])]))
    
    def _connecting_0_guard(self, parameters):
        socket = parameters[0]
        return self.socket == socket
    
    def _connected_listening_listen_0_exec(self, parameters):
        socket = parameters[0]
        data = parameters[1]
        self.received_data += data
    
    def _connected_listening_listen_0_guard(self, parameters):
        socket = parameters[0]
        data = parameters[1]
        return (self.socket == socket) and (len(data) > 0)
    
    def _connected_listening_listen_1_guard(self, parameters):
        socket = parameters[0]
        data = parameters[1]
        return (self.socket == socket) and (len(data) == 0)
    
    def _connected_sending_waiting_for_data_0_exec(self, parameters):
        self.big_step.outputEvent(Event("send_socket", "socket_out", [self.socket, self.send_data]))
    
    def _connected_sending_waiting_for_data_0_guard(self, parameters):
        return len(self.send_data) > 0
    
    def _connected_sending_transferring_0_exec(self, parameters):
        socket = parameters[0]
        sent_bytes = parameters[1]
        self.send_data = self.send_data[sent_bytes:]
    
    def _connected_sending_transferring_0_guard(self, parameters):
        socket = parameters[0]
        sent_bytes = parameters[1]
        return self.socket == socket
    
    def _connected_queueing_queueing_0_exec(self, parameters):
        data = parameters[0]
        destination = parameters[1]
        self.send_data += "POST / HTTP/1.0\r\n"
        self.send_data += "Content-Length: %i\r\n" % len(str(data))
        self.send_data += "\r\n"
        self.send_data += data
        self.destinations.append(destination)
    
    def _connected_parsing_wait_for_header_0_exec(self, parameters):
        header, self.received_data = self.received_data.split("\r\n\r\n", 1)
        header = header.lower()
        if "content-length" in header:
            _, after = header.split("content-length:", 1)
            after, _ = after.split("\r\n", 1)
            after = after.strip()
            self.length = int(after)
        else:
            self.length = float('inf')
    
    def _connected_parsing_wait_for_header_0_guard(self, parameters):
        return '\r\n\r\n' in self.received_data
    
    def _connected_parsing_wait_for_payload_0_exec(self, parameters):
        data = self.received_data[:self.length]
        self.received_data = self.received_data[self.length:]
        #params = dict([p.split('=') for p in data.split('&')])
        #data = {k: urllib.unquote_plus(v) for k, v in params.iteritems()}
        self.big_step.outputEventOM(Event("narrow_cast", None, [self, self.destinations.pop(0), Event("HTTP_output", None, [data])]))
    
    def _connected_parsing_wait_for_payload_0_guard(self, parameters):
        return len(self.received_data) >= self.length
    
    def initializeStatechart(self):
        # enter default state
        self.default_targets = self.states["/init"].getEffectiveTargetStates()
        RuntimeClassBase.initializeStatechart(self)

class ObjectManager(ObjectManagerBase):
    def __init__(self, controller):
        ObjectManagerBase.__init__(self, controller)
    
    def instantiate(self, class_name, construct_params):
        if class_name == "Prompt":
            instance = Prompt(self.controller)
            instance.associations = {}
            instance.associations["to_server"] = Association("HTTPClient", 1, 1)
        elif class_name == "HTTPClient":
            instance = HTTPClient(self.controller, construct_params[0], construct_params[1])
            instance.associations = {}
            instance.associations["parent"] = Association("Prompt", 1, 1)
        else:
            raise Exception("Cannot instantiate class " + class_name)
        return instance

class Controller(ThreadsControllerBase):
    def __init__(self, keep_running = None, behind_schedule_callback = None):
        if keep_running == None: keep_running = True
        if behind_schedule_callback == None: behind_schedule_callback = None
        ThreadsControllerBase.__init__(self, ObjectManager(self), keep_running, behind_schedule_callback)
        self.addInputPort("socket_in")
        self.addOutputPort("socket_out")
        self.object_manager.createInstance("Prompt", [])