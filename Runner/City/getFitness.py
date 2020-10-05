# getFitness determines the desnity fitness of the simulation.
# Author: Josh Pike

#Department of Transport, road traffic statistics, Annual Average daily flow 2018
#"All motor vehicles" number is divided by 24 to represent an hour.  
A257 = 780    # https://roadtraffic.dft.gov.uk/manualcountpoints/26109
A290_0 = 1570 # https://roadtraffic.dft.gov.uk/manualcountpoints/36105
A290_1 = 662  # https://roadtraffic.dft.gov.uk/manualcountpoints/6103
BrdStrt = 959 # https://roadtraffic.dft.gov.uk/manualcountpoints/99206

#analyse() compares real and simulated traffic values
def analyse(num, total):
    road = {
            1: A257,
            2: A290_0,
            3: A290_1, 
            4: BrdStrt
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
    output = open("TempData/Other/Canterbury.out.xml", "r")
    
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
    while beg < end:
        total += int(lines[beg])
        beg += 1
    return total  

def main():
    results = []
    lines = []
    lines = getOutput(lines)
    listLength = len(lines)    
    num = 0
    
    if listLength < 12:
        print("ERROR: List too short")
    else:        
        total = []                
        total.append(getDetectorTotal(lines, 0, 3))
        total.append(getDetectorTotal(lines, 4, 7))
        total.append(getDetectorTotal(lines, 8, 9))
        total.append(getDetectorTotal(lines, 10, 11))
        n=0
        while n < 4:            
            results.append(analyse(n+1, total[n]))
            n+=1
        num = getFitness(results)    
    return num