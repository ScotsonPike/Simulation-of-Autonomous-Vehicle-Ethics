#DataRun create a SUMO configFile for a particular Data file as well as loading in the files breakpoints into the simulation
#Author: Joshua Pike
import Runner

class DataRun:
    net = '"Thanet.net.xml"'
    configFile = ""
    sumocfgName = "runSimData.sumocfg"
    
    def __init__(self, path):   
        self.path = path
    
    #setPath() concatenates the correct path into the config file
    def setPath(self):
        self.configFile = '<configuration>\n	<input>\n		<net-file value='+self.net+'/>\n		<route-files value="'+self.path+'/vehicle2.trip.xml, '+self.path+'/pCar.trip.xml, '+self.path+'/truck.trip.xml, '+self.path+'/lorry.trip.xml, '+self.path+'/motorcycle.trip.xml, '+self.path+'/pt.rou.xml, '+self.path+'/moped.trip.xml, '+self.path+'/bike.trip.xml, '+self.path+'/ped.trip.xml, '+self.path+'/bus.rou.xml"/>\n		<additional-files value="TempData/Add/Thanet.poly.xml, TempData/Add/Thanet.add.xml,  TempData/Add/Parking.add.xml"/>\n	</input>\n	<time>\n		<begin value="0"/>\n		<end value="3600"/>\n	</time>\n</configuration>'
        
    def writeFile(self):        
        f = open(self.sumocfgName, "w")
        f.write(self.configFile)
        f.close()
        
    def getBreakpoints(self):
        fileName = path + "//Breakpoints.txt"
        f = open(fileName, "r")
        for x in f:
            self.breakpoints = x
    
    def run(self):        
        r = Runner.Runner(self.net, self.sumocfgName)
        r.runGui(self.breakpoints)
    
if __name__ == "__main__":
    simName = input("Enter simulation name: ")
    path = "Data1//"+simName # change path to "Data//" if this folder is required.
    dr = DataRun(path)
    dr.setPath()
    dr.writeFile()
    dr.getBreakpoints()
    dr.run()
