#DataRun create a SUMO configFile for a particular Data file as well as loading in the files breakpoints into the simulation
#Author: Joshua Pike
import Runner

class DataRun:
    net = "Canterbury.net.xml"
    configFile = ""
    sumocfgName = "runSimData.sumocfg"
    
    def __init__(self, path):
        self.path = path
        
    #setPath() concatenates the correct path into the config file        
    def setPath(self):
        self.configFile = '<configuration>\n	<input>\n		<net-file value="Canterbury.net.xml"/>\n		<route-files value="'+self.path+'/vehicle.trip.xml, '+self.path+'/pCar.trip.xml, '+self.path+'/truck.trip.xml, '+self.path+'/lorry.trip.xml, '+self.path+'/motorcycle.trip.xml, '+self.path+'/pt.rou.xml, '+self.path+'/pt2.rou.xml, '+self.path+'/moped.trip.xml, '+self.path+'/bike.trip.xml, '+self.path+'/ped.trip.xml"/>\n		<additional-files value="TempData/Add/Canterbury2.poly.xml, TempData/Add/TrainStations.add.xml, TempData/Add/BusStops.add.xml, TempData/Add/Parking.add.xml, TempData/Add/Detectors.add.xml"/>\n	</input>\n	<time>\n		<begin value="0"/>\n		<end value="3600"/>\n	</time>\n</configuration>'
        
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
