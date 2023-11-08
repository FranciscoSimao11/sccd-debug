SCCD

Generation of code from xml - COMPILER

Receive model as an input xml file and optional arguments:
. target language: Python | Javascript | C++
. platform: threads | eventloop | gameloop
. output: path to the generated file
. verbose: ...

From the xml, generate the Abstract Syntax Tree (AST). Using this AST, it is then possible to obtain a generic object. From the generic object, we can write the code in the target language and generate a file in accordance to the provided model.

XML -> AST

(xmlToSccd)

INITIALIZING THE CLASS DIAGRAM
- parse the classes, ports and other xml elements in the xml file
- for each class, create a class object providing the xml class element as well as the whole class diagram
- inside the class object, the variables are set and the process method is called
- in this method, the ports, relationships, attributes, methods, constructors, destructors and the statechart are set

INITIALIZING THE STATECHARTS
- to create the statechart object, the associated class and statechart xml element are provided
- the root of the statechart is created and initialized as a statechart node object, so the statechart is built recursively as each node is initialized until there are no more nodes in the hierarchy
- the semantic options are chosen based on the default values or in the provided xml model
- the states are recursively found as well the transitions:
- history states are calculated

- each statechart node is initialized
- each node has access to the statechart object, to its parent and to its children
- each node is parsed to check its type, resolve its name, parse its enter and exit actions
- its transitions are generated and analyzed and its children are generated (a.k.a. more statechart nodes are created)
- its initial states are also defined

- each transition receives its xml element as well as the node from where it leaves
- the triggerEvent object is created as well as the expression for the guard condition and the target is set through the StateReference object
- enter/exit nodes are set later when the transitions are performed

state linker - visitor fixing state references

path calculator - visitor calculating paths

(sccdToGeneric)

- according to the chosen platform, a generic class is generated.
- the generic code generated here is responsible for the structure of the generated code, including the generated methods (for constructors, statechart structure and user defined methods). This is where the statechart runtime code is built so it is used in the generated code to generate the correct statechart. The generic code will include the problem-related classes as well as the object manager and controller classes.

(genericToTarget)

- from the generic class, the code will be written to a file in target language


Statechart execution

- enter state (action)
- event/timer
fire - exit state (action)
fire - transition (action)
fire - enter state (action)

config update? I should use self.configuration instead of self.current_state. However self.configuration seems to lag behing the actual current state.

RuntimeClassBase

step -> big_step -> combo_step -> small_step -> fire()

ObjectManager?

ObjectManagerBase has a set of RuntimeClassBase instances




"Alternatively, by instrumenting the model, you can also apply a scaling factor to all transitions to mimic scaled real-time, but then you cannot change the scaling factor during execution. It's also not possible to change execution speed to "as-fast-as-possible" by instrumentation alone: you cannot set all "after"s to 0, because then transitions could fire in a different order and this would change the meaning of the model."

"For instance, if we want to use our model in TkInter code (Python), or in a web browser (JS), both already have an event loop that SCCD can make use of via the "event loop" simulation type. With an event loop, there is a single thread, that looks for "due" events (events are timestamped), and handles them. If there are no due events, but the event queue is not empty, the process will sleep until the next event is due. If the queue is empty, the process sleeps until it is woken up by an input event.

When there is no event loop in place, the "threads" simulation type will simply run the simulation in a separate thread, and use Python's native sleep function.

The "game loop" simulation type simply lets you advance simulated time in custom increments. In the old days (and maybe still today), a video game had a main loop, that would (1) check the state of input devices (mouse, keyboard, joystick, ...), generating necessary input "events", (2) advance simulated time (processing inputs, updating the state of the game), (3) render a frame based on the new state of the game, and (4) switch framebuffers ("double buffering"), every 1/60th of a second. Also here, there is only a single thread."