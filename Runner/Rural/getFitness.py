# getFitness determines the desnity fitness of the simulation.
# Author: Josh Pike

#Department of Transport, road traffic statistics, Annual Average daily flow 2018
#"All motor vehicles" number is divided by 24 to represent an hour.  
CanterburyRd = 683 #16389/24 https://roadtraffic.dft.gov.uk/manualcountpoints/16282
A299 = 867         #20805/24 https://roadtraffic.dft.gov.uk/manualcountpoints/36915
SpitfireWay = 280  #6708/24  https://roadtraffic.dft.gov.uk/manualcountpoints/940988
A253 = 252         #6043/24  https://roadtraffic.dft.gov.uk/manualcountpoints/16796

#analyse() compares real and simulated traffic values
def analyse(num, total):
    road = {
            1: A253,
            2: A299,
            3: CanterburyRd,
            4: SpitfireWay
            }
    
    real = road.get(num)     
    result = total / real
    result = round(result,1)    
    return result

#getFitness() produces the mean of the four density fitnesses collected. 
def getFitness(results):
    total = 0
    for x in results:
        total += x
    fitness = total/4
    fitness = round(fitness,2)    
    return fitness

#getOutput() retrieves the information from a simulations output file and stores the "nVehEntered" number from each string in lines[]
def getOutput(lines):    
    output = open("TempData/Other/Thanet.out.xml", "r") 
    
    for x in output:         
        line = x.rstrip('\n')
        num = line.find("nVehEntered") 
        if num >= 0:
            lines.append(line)
                   
    list=[]
    for x in lines:
        line = x.split('nVehEntered="', 1)[-1].split('"', -1)
        list.append(line)
    
    lines.clear()
    for x in list:          
        lines.append(x[0])     
    return lines

#getDetectorTotal() addes up the "nVehEntered" number for detectors next to one another
def getDetectorTotal(lines, beg, end):
    total = 0
    while beg <= end:
        total += int(lines[beg])
        beg += 1
    return total  

def main():
    results = []
    lines = []
    lines = getOutput(lines)
    listLength = len(lines)    
    num = 0
    
    if listLength < 10:
        print("ERROR: List too short - "+str(listLength))
    else:        
        total = []                
        total.append(getDetectorTotal(lines, 0, 1))
        total.append(getDetectorTotal(lines, 2, 5))
        total.append(getDetectorTotal(lines, 6, 7))
        total.append(getDetectorTotal(lines, 8, 9))
        n=0
        while n < 4:            
            results.append(analyse(n+1, total[n]))
            n+=1
        num = getFitness(results)    
    return num