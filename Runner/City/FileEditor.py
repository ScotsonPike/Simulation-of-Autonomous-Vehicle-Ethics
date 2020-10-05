# This script returns the number of emergency breaking warnings, a string of breakpoints and the number of teleport warnings tallied in the simulation.
# The script also creates a file contanting the results of the simulation. 
# Author: Josh Pike
import shutil
import os
import datetime  

class FileEditor:    
    teleports = 0  
    collisionWarnings = 0
    warnings = 0
    breakpoints = ''
    fileName = ''
    dirName = ''
    dir = ''
    path = ''
    errorList = []
    timeStamps = []
    
    def __init__(self, simTime, fitness):
        self.simTime = simTime
        self.fitness = fitness        
            
    def getCollisionWarnings(self):        
        return self.collisionWarnings
    
    def getTeleports(self):
        return self.teleports
        
    def getWarnings(self):
        return self.warnings
        
    #Get Output file and extract only emergenct breaking errors, teleport errors are tallied.
    def getOutput(self):
        lines = []
        output = open("TempData/Other/error.txt")
        self.teleports = 0
        for x in output:
            lines.append(x.rstrip('\n'))
        for x in lines:
            num0 = x.find("emergency")
            num1 = x.find("collision")
            num2 = x.find("teleport")

            if num0 >= 0 or num1 >= 0:            
                self.errorList.append(x)
                self.warnings += 1
            if num1 >= 0:
                self.collisionWarnings += 1
            if num2 != -1:
                self.teleports+=1
                
    def setFitness(self, fitness):
        self.fitness = fitness
    
    #Write readable text file with results 
    def writeFile(self):
        #check if file name already exists
        self.fileName = "sim.txt"
        self.path = "TempData\\Other\\Data\\" 
        path = self.path + self.fileName
        if os.path.isfile(path):
            expand = 0
            while True:
                expand += 1
                newfileName = self.fileName.split(".txt")[0] + str(expand) + ".txt"
                path = self.path + newfileName
                if os.path.isfile(path):
                    continue
                else:                    
                    self.fileName = newfileName
                    break
        #write file  
        path = self.path + self.fileName
        f = open(path, "x") # with open file
        f.write(str(datetime.datetime.now()) + "\n \n")
        f.write("Total Sim Time: " + str(self.simTime)+"\n")
        f.write("Fitness       : " + str(self.fitness)+"\n\n")
        f.write("Total Warnings: " + str(self.warnings)+"\n")
        f.write("Teleports     : " + str(self.teleports)+"\n")
        f.write("Collisions    : " + str(self.collisionWarnings)+"\n\n")
        
        for x in self.errorList:
            f.write(x +"\n")
        f.close()
        
        self.errorList.clear()

    #create a new dir for route results   
    def copyDir(self):    
        self.dirName = "Data1\\Sim" 
        if os.path.isdir(self.dirName):
            expand = 0
            while True:
                self.dirName = "Data\\Sim" 
                expand += 1                
                newDirName = self.dirName + str(expand)  
                if self.collisionWarnings > 0:                    
                    newDirName += "C"
                alt = newDirName+"C"                
                if os.path.isdir(newDirName) or os.path.isdir(alt):                    
                    continue                
                else:
                    self.dirName = newDirName                    
                    break
        command = "mkdir "+ self.dirName          
        shutil.copytree("TempData\\Rou", self.dirName)        
    
    def copyFile(self):
        destFile = "Data1/" + self.dir + "/"+self.fileName         
        if not os.path.isfile(destFile):         
            command = "copy TempData\\Other\\Data\\" + self.fileName + " " +self.dirName
            os.system(command)

    #get useable time values from errorlog
    def getTimeStamps(self):    
        for x in self.errorList:
            line = x.split('time', 1)[-1]
            line = line.strip()
            # remove additional symbols
            if line.endswith('.') or line.endswith('"'):
                line = line[:-1]
            if line.startswith('='):            
                line = line.strip('=')
            if line.find('move=stage'):
                line = line.strip('move=stage')
            if line.find('stage=laneChan'):
                line = line.strip('stage=laneChan')
            self.timeStamps.append(line)

    #concatenate timeStamps into a single string
    def setBreakpoints(self):
        self.breakpoints = '"'
        for x in self.timeStamps:
            self.breakpoints += x + ", "
        self.breakpoints = self.breakpoints[:-2]
        self.breakpoints += '"'
        self.timeStamps.clear()
            
    def writeBreakPointFile(self):
        self.fileName = self.dirName+"//Breakpoints.txt"
        f = open(self.fileName, "x")
        f.write(self.breakpoints)        
        f.close()        