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
Executable builds into ~/build/ . For example, to run test from current directory 
in cli: <br>
`build/test`

## Import Native Source in CLion
Once you have cloned the project to your local repo:
1) Select `Import Project from Sources` from the CLion main menu.
2) Select the `~/student-hub/studenthub/academics/scheduler/native` directory. 
Press `ok` button.
3) Make sure the `src` directory and all files and sub-directories are checked. 
Press `ok` button.

## Update .gitignore as needed
Keep the source tree clean of system specific project files/settings and build
files/artifacts. Some common files types/directories are already added to the project .gitignore
file. Please update as needed.

## Unit Testing
Unit tests are implemented using the Catch framework. 

Catch2 is a multi-paradigm test framework for C++. which also supports Objective-C 
(and maybe C). It is primarily distributed as a single header file, although certain 
extensions may require additional headers. <br>
https://github.com/catchorg/Catch2

catchorg/Catch2 is licensed under the
Boost Software License 1.0

A simple permissive license only requiring preservation of copyright and license 
notices for source (and not binary) distribution. Licensed works, modifications, 
and larger works may be distributed under different terms and without source code.

Boost Software License - Version 1.0 - August 17th, 2003

Permission is hereby granted, free of charge, to any person or organization
obtaining a copy of the software and accompanying documentation covered by
this license (the "Software") to use, reproduce, display, distribute,
execute, and transmit the Software, and to prepare derivative works of the
Software, and to permit third-parties to whom the Software is furnished to
do so, all subject to the following:

The copyright notices in the Software and this entire statement, including
the above license grant, this restriction and the following disclaimer,
must be included in all copies of the Software, in whole or in part, and
all derivative works of the Software, unless such copies or derivative
works are solely in the form of machine-executable object code generated by
a source language processor.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE, TITLE AND NON-INFRINGEMENT. IN NO EVENT
SHALL THE COPYRIGHT HOLDERS OR ANYONE DISTRIBUTING THE SOFTWARE BE LIABLE
FOR ANY DAMAGES OR OTHER LIABILITY, WHETHER IN CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.