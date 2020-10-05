#Author: Joshua Pike
import time
import Runner
import getFitness
import FileEditor

class SimRun:
    """
    A class used to perform multiple SUMO simulations and save their data
    Attributes
    ----------
    simNum : int
        How many simulations will be run
    net : str
        The .net.xml file used in SUMO
    runFile : str
        The .sumocfg used to execute SUMO 
    
    Methods
    -------
    run()
        Performs a while loop which runs a SUMO simulation and saves it's data if collisions occur.
    """
    
    def __init__(self, simNum, net, runFile):
        """
        Parameters
        ----------
        simNum : int
            Number of simulations the program will execute
        net : str
            The .net.xml file
        runFile : str
            The .sumocfg file 
        """
        
        self.simNum = simNum
        self.net = net
        self.runFile = runFile
         
    def run(self):
        r = Runner.Runner(self.net, self.runFile)        
        i = 0
        while i < self.simNum:        
            #start simulation and log simTime 
            print("Count: "+str(i))
            startTime = time.time()
            r.createRandomTrips()            
            r.runNoGui()            
            simTime = time.time() - startTime  
            
            #Analyse for traffic density fitness
            densityFitness = getFitness.main()
            
            #Create FileEditor object
            f = FileEditor.FileEditor(simTime, densityFitness)            
            f.getOutput()
            f.getTimeStamps() 
            f.setBreakpoints()            
            f.writeFile() 
            
            if f.getTeleports() > 0:
                fitness = round((densityFitness / f.getTeleports()), 2)                
            else:
                fitness = densityFitness 
            f.setFitness(fitness)  
            
            print("SimRun F: "+str(fitness))   
            #if collisions occur copy route data, warning file and breakpoint file
            print("Collision Num: "+str(f.getCollisionWarnings()))
            if f.getWarnings() > 0 and f.getTeleports() < 10:
                f.copyDir()
                f.copyFile()
                f.writeBreakPointFile()
            i+=1             
#os.expandUse            
if __name__ == "__main__":
    net = "Canterbury.net.xml"
    run = "run.sumocfg"
    sr = SimRun(1000, net, run)
    sr.run()