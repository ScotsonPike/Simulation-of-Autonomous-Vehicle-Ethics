﻿# Simulation-of-Autonomous-Vehicle-Ethics

This project aims to simulate autonomous vehicles using the microscopic traffic simulator SUMO. The Video folder contains examples of the simulation in action. The Runner folder contains the Python scripts used to create all of the data collected.
The Runner directory contains both the City and Rural simulations.

Within Data directories, subdirectories marked with a “C” e.g. “Sim97C” contain at least one collision. These collisions are collected to track the frequency of potential ethical problems that may occur in a network of autonomous vehicles. Collisions occur in SUMO whenever the gaps between vehicles are reduced below the “minGap” parameter of another vehicle. This has been set to 1m to include potential near misses. When a collision occurs the vehicles will wait for 50 time steps before proceeding with their route. Each collision produces a warning message which is stored by the FileEditor.py script. Emergency breaking warning messages are also collected and added to the breakpoint file.

Installation
Python is required to run python scripts

Download SUMO 
https://www.eclipse.org/sumo/

Set SUMO_HOME environment
https://sumo.dlr.de/docs/Basics/Basic_Computer_Skills.html#additional_environment_variables

Usage
simRun.py - creates simulations data, creating a directory containing the trip files necessary to repeat each simulation. This new folder also contains a set of breakpoints to allow the user to visit any warning messages such as collisions. The folder will also contain a document with relevant simulation data, number of collisions, teleports* etc. This file name does not correspond with the folder name but will contain the correct information for that directory.  
 
DataRun.py - This script creates and executes a SUMO configuration file, "runSimData.sumcfg", using the trip files in the desired simulation. The script requests the simulation name e.g "Sim97C", which will write the configuration file with the correct path. The simulation will also load the relevant breakpoint file. These breakpoints feature all emergency breaking and collisions warnings. 

geneticAlgorithm.py - this script has been used to find the appropriate number of vehicles to add to each simulation. The fitness function has been decided by comparing the total number of vehicles crossing detectors in the simulation against the traffic statistics taken by the Department for Transport, this is then divided by the number of teleports to penalise simulations which have too much congestion.

*teleports occur when vehicles are unable to move, this generally happens in a grid lock, this kind of congestion occurs when a simulation has too many vehicles and will reduce the usablity of the simulation due to the unnatural movement of the vehicles. 
