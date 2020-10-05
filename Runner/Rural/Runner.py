#Runner is used to create trip files for the simulation using the SUMO tool randomTrips.py,
#Author: Joshua Pike

from __future__ import absolute_import
from __future__ import print_function
import os
import sys
import time

# Lines 11-19 are from the following scource:
# https://sumo.dlr.de/docs/TraCI/Interfacing_TraCI_from_Python.html

if 'SUMO_HOME' in os.environ:
        tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
        sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")   
             
import traci    
from sumolib import checkBinary    
import randomTrips

class Runner(object):       

    def __init__(self, net, run):
        self.net = net
        self.run = run        
    
    def createRandomTrips(self):
        randomTrips.main(randomTrips.get_options([
            '--net-file', self.net,
            '--output-trip-file',
            'TempData/Rou/ped.trip.xml',
            '--prefix','ped', 
            '--persontrips',            
            '-e', '4000',
            '-p', '1.5',
            '--random',
            '--validate'
        ]))
        randomTrips.main(randomTrips.get_options([
            '--net-file', self.net,
            '--output-trip-file',
            'TempData/Rou/pCar.trip.xml',
            '--prefix','pCar',
            '--persontrips',
            '--trip-attributes', 'modes="public car"',
            '-e', '4000',
            '-p', '1.5',
            '--random',
            '--validate'
        ]))
        randomTrips.main(randomTrips.get_options([
        '--net-file', self.net,
        '-o', 'TempData/Rou/vehicle.trip.xml',
        '--prefix', 'veh',
        '--trip-attributes', 'personNumber="2"',
        '-e', '4000',
        '-p', '1.25',
        '--random',
        '--validate'
        ]))
        randomTrips.main(randomTrips.get_options([
        '--net-file', self.net,
        '-o', 'TempData/Rou/truck.trip.xml',
        '--prefix', 'truck',
        '--vehicle-class', 'truck',
        '-e', '5000',
        '-p', '20',
        '--random',
        '--validate'
        ]))
        randomTrips.main(randomTrips.get_options([
        '--net-file', self.net,
        '-o', 'TempData/Rou/lorry.trip.xml',
        '--prefix', 'trailer',
        '--vehicle-class', 'trailer',
        '-e', '5000',
        '-p', '100',
        '--random',
        '--validate'
        ]))
        randomTrips.main(randomTrips.get_options([
        '--net-file', self.net,
        '-o', 'TempData/Rou/motorcycle.trip.xml',
        '--prefix', 'motorcycle',
        '--vehicle-class', 'motorcycle',
        '-e', '5000',
        '-p', '25',
        '--random',
        '--validate'
        ]))
        randomTrips.main(randomTrips.get_options([
        '--net-file', self.net,
        '-o', 'TempData/Rou/moped.trip.xml',
        '--prefix', 'moped',
        '--vehicle-class', 'moped',
        '-e', '5000',
        '-p', '30',
        '--random',
        '--validate'
        ]))
        randomTrips.main(randomTrips.get_options([
        '--net-file', self.net,
        '-o', 'TempData/Rou/bike.trip.xml',
        '--prefix', 'bik',
        '--vehicle-class', 'bicycle',
        '-e', '5000',
        '-p', '30',
        '--random',
        '--validate'
        ]))        
    
    def runNoGui(self):          
        fileName = 'sumo -c '+self.run+' --collision.action warn --collision.mingap-factor 1 --collision.stoptime 50 --error-log TempData/Other/error.txt -W True'   
        os.system(fileName)             
               
    def runGui(self, breakpoints):          
        fileName = 'sumo-gui -c '+self.run+' --collision.action warn --collision.mingap-factor 1 --collision.stoptime 50 --breakpoints '+breakpoints   
        os.system(fileName)       
        
    def runNoBreak(self):          
        fileName = 'sumo-gui -c '+self.run+' --collision.action warn --collision.mingap-factor 1 --collision.stoptime 50 --start'   
        os.system(fileName) 

class DynamicRunner(Runner):

    def createRandomTrips(self, pop):
        randomTrips.main(randomTrips.get_options([
            '--net-file', self.net,
            '--output-trip-file',
            'TempData/Rou/ped.trip.xml',
            '--prefix','ped', 
            '--persontrips',            
            '-e', '4000',
            '-p', '1.93',
            '--random',
            '--validate'
        ]))
        randomTrips.main(randomTrips.get_options([
            '--net-file', self.net,
            '--output-trip-file',
            'TempData/Rou/pCar.trip.xml',
            '--prefix','pCar',
            '--persontrips',
            '--trip-attributes', 'modes="public car"',
            '-e', '4000',
            '-p', pop[0],
            '--random',
            '--validate'
        ]))
        randomTrips.main(randomTrips.get_options([
        '--net-file', self.net,
        '-o', 'TempData/Rou/vehicle.trip.xml',
        '--prefix', 'veh',
        '--trip-attributes', 'personNumber="2"',
        '-e', '4000',
        '-p', pop[1],
        '--random',
        '--validate'
        ]))
        randomTrips.main(randomTrips.get_options([
        '--net-file', self.net,
        '-o', 'TempData/Rou/truck.trip.xml',
        '--prefix', 'truck',
        '--vehicle-class', 'truck',
        '-e', '5000',
        '-p', '20',
        '--random',
        '--validate'
        ]))
        randomTrips.main(randomTrips.get_options([
        '--net-file', self.net,
        '-o', 'TempData/Rou/lorry.trip.xml',
        '--prefix', 'trailer',
        '--vehicle-class', 'trailer',
        '-e', '5000',
        '-p', '100',
        '--random',
        '--validate'
        ]))
        randomTrips.main(randomTrips.get_options([
        '--net-file', self.net,
        '-o', 'TempData/Rou/motorcycle.trip.xml',
        '--prefix', 'motorcycle',
        '--vehicle-class', 'motorcycle',
        '-e', '5000',
        '-p', '25',
        '--random',
        '--validate'
        ]))
        randomTrips.main(randomTrips.get_options([
        '--net-file', self.net,
        '-o', 'TempData/Rou/moped.trip.xml',
        '--prefix', 'moped',
        '--vehicle-class', 'moped',
        '-e', '5000',
        '-p', '30',
        '--random',
        '--validate'
        ]))
        randomTrips.main(randomTrips.get_options([
        '--net-file', self.net,
        '-o', 'TempData/Rou/bike.trip.xml',
        '--prefix', 'bik',
        '--vehicle-class', 'bicycle',
        '-e', '5000',
        '-p', '30',
        '--random',
        '--validate'
        ]))