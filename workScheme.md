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




QUESTIONS
- line 444 - sccd constructs, why is parent passed as None? Is it just none if it's not passed?
- Subactions, a bit confusing? Expressions?
- maybe some better explanation of state linker, path calculator and super class linker would be useful
- i'm a bit confused on some aspects, particularly the visitor functions/classes and the conversion from the class diagram to the generic and the generic to the target language

- how can i test my changes? i need to run the setup and install everytime I want to see the changes, why is that? also I also cant generate the same file I have just generated unless I change its name or delete the previous one. //update: i made a small script to install everytime i want to test changes but it seems a bit silly to do this 