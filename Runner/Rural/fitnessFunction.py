#The fitnessFunction class runs simulation and produces a fitness function based on the fitness of the traffic density divided by the number of teleports. Teleports occur when a simulation is congested therefore these simulations are penalised. 
#Author: Joshua Pike
import time
import Runner
import getFitness
import FileEditor
import RouteChanger

class fitnessFunction:
        
    net = "Thanet.net.xml"
    runFile = "run.sumocfg"    
    
    def __init__(self, pop):
        self.pop = pop
         
    def run(self):
        r = Runner.DynamicRunner(self.net, self.runFile)        
        i = 0

        #start simulation and log simTime           
        startTime = time.time()
        r.createRandomTrips(self.pop) 
        rc = RouteChanger.RouteChanger()
        rc.getFile()
        rc.writeFile()
        r.runNoGui()  #   r.runNoGui()       
        simTime = time.time() - startTime  
          
        #Analyse for traffic density fitness
        densityFitness = getFitness.main()
           
        #Create FileEditor object
        f = FileEditor.FileEditor(simTime, densityFitness)            
        f.getOutput()
        f.getTimeStamps() 
        #f.setBreakpoints()            
        #f.writeFile() 
                               
        if f.getTeleports() > 0:
          
            fitness = round((densityFitness / f.getTeleports()), 2)            
            print("Fitness: "+str(fitness))
        else:
            fitness = densityFitness 
        print("Fit: "+str(fitness))
        print(str("Teleports: "+str(f.getTeleports())))
            
        return fitness