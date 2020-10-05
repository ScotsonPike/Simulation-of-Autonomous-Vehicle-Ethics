#RouteChanger is used to create a more realistic traffic flow by rerouting half of the vehicles towards the major highways.
#Author: Joshua Pike 
import random

class RouteChanger:
    
    lines=[]
    
    #getFile() opens and edits a vehicle file to change the to and from addresses of certain vehicles. 
    def getFile(self):
        #f = open("tempData//Rou//vehicle.trip.xml")
        
        with open("tempData//Rou//vehicle.trip.xml", 'r') as file
        f = file.readlines()
        
        i=0
        for x in f:                        
            if i % 2 == 0:
                num = random.random()                
                if num < 0.33:
                    if x.find("trip"):
                        line = x.split('to=')     
                        line[0] += 'to="146918228#5"/>\n'  
                        self.lines.append(line[0]) 
                elif num < 0.66:
                    if x.find("trip"):
                        line = x.split('to=')     
                        line[0] += 'to="-71093886#0"/>\n'  
                        self.lines.append(line[0])                     
                else:
                    if x.find("trip"):
                        line = x.split('from=') 
                        line1 = x.split('from=', 1)[-1]
                        line1 = line1.split('to=')[-1]
                        line1 = " to="+line1
                        line[0] += 'from="146918225#0"' + line1                        
                        self.lines.append(line[0]) 
            else:
                self.lines.append(x)
            i+=1
        #f.close()
        self.lines.pop(2)        
        del self.lines[0:29]
        
    def writeFile(self):
        f = open("tempData//Rou//vehicle2.trip.xml", "w")  
        
        f.write("<routes>\n")
        for x in self.lines:            
            if x.find("trip"):
                f.write(x)                
        f.write("</routes>")
        f.close() 
        lines.clear()
