#Author: Joshua Pike
import time
import Runner
import getFitness
import FileEditor
import RouteChanger

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
            print("Count: "+str(i))
            #start simulation and log simTime           
            startTime = time.time()
            r.createRandomTrips()   
            rc = RouteChanger.RouteChanger()
            rc.getFile()
            rc.writeFile()
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
            print("Tel: "+str(f.getTeleports()))
            print("Fit: "+str(fitness))
            
            #if collisions occur copy route data, warning file and breakpoint file
            print("Collision Num: "+str(f.getCollisionWarnings()))
            f.setFitness(fitness)
            if f.getWarnings() > 0:
                f.copyDir()
                f.copyFile()
                f.writeBreakPointFile()                        
            i+=1         
                      
if __name__ == "__main__":
    net = "Thanet.net.xml"
    run = "run.sumocfg"
    simNum = 100
    sr = SimRun(simNum, net, run)
    sr.run()