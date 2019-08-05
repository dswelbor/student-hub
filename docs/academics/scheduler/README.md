# Class Scheduler
This app models data for college Majors and required courses. It automatically generates 
a class schedule based on a combination of 8 and 16 week terms, balancing predicted 
course difficulty and prioritizing "gatekeeper" courses. This app interfaces with a 
native class scheduling app, implemented in C++. This native program internally represents 
courses as Nodes and pre-reqs as edges in a Directed Graph.

## Functional Requirements
Users can self-identify Major choice and completed courses. Users can also 
self assess course difficulty. Users would be able select preferred per-semester credit 
hours and course "difficulty".

## Native C/C++ Source 
The logic for this app is written in C++. The source code for the app is located in 
~/native/src . To install build tools for make and g++ enter the following from 
commandline: <br>
`sudo apt install build-essential`

## Build Application from Source
From commandline, navigate to ~/native/ from repository root: <br>
`cd studenthub/academics/scheduler/native` <br>
Run makefile: <br>
`make` <br>
Executable builds into ~/build/ . For example, to run digraph_test from current directory 
in cli: <br>
`build/digraph_test`

## Update .gitignore as needed
Try to keep the source tree clean of system specific project files/settings and build
files/artifacts. Some common files types/directories are already added to the project .gitignore
file. Please update as needed.