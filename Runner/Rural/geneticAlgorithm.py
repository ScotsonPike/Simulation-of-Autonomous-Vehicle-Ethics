# A genetic Algorithm to find the best ratio between vehicle and pedestrian trips when compared to real traiffic data.
# fitness = (sim data / real data), mean result of four detectors
# Author: Josh Pike

import fitnessFunction
import random

#creates an initial population of members
def createNewPop(popSize):
    pop = []
    i=0
    while i < popSize:
        member = createNewMember()
        pop.append(member)
        i+=1
    return pop

#creates a pair of numbers to input into the simulation
def createNewMember():
    member = []
    i=0
    while i < 2:
        num = round(random.uniform(0.5, 5), 2)
        member.append(num)
        i+=1
    return member

# Gets the fitness of each member and places into a new array 
def createFitnessArray(pop, popSize, fitness):
    i=0
    fitnessArray = []
    while i < popSize:
        function = fitnessFunction.fitnessFunction(pop[i])
        fitness = function.run()
        fitnessArray.append([pop[i], fitness])
        print("Combined Fitness: " + str(fitness))
        i+=1   
    return fitnessArray

# Sorts the new array by the fitness of each member lowest(best) fitness at position 0 
def sort(fitnessArray):
    fitnessArray = sorted(fitnessArray,key=lambda l:l[1], reverse=True)
    return fitnessArray

#randomly selects a number from the fitnessArray    
def selection(fitnessArray):
    cutOff = round(len(fitnessArray)) #/2
    num = random.randrange(0, cutOff)    
    member = fitnessArray[num]
    return member

#section 
def acceptReject(fitnessArray):
    maxFitness = fitnessArray[0][1]

    count = 0
    while True:
        r1 = random.randrange(len(fitnessArray))
        r2 = random.uniform(0, maxFitness)
        partner = fitnessArray[r1]

        if r2 < partner[1]:
            return partner   
        count+=1
    if count == 10000:
        print("ERROR: acceptReject()")
        False 

#selects a pair for tournament and then calls the tournament function
def getTournamentPair(fitnessArray):
    pair = []
    i = 0
    while i < 2:
        notFinished = True
        while notFinished:
            a = acceptReject(fitnessArray)
            b = acceptReject(fitnessArray)
            
            if a == b:
                b = selection(fitnessArray)
            else:
                notFinished = False
                
        victor = tournament(a, b)
        pair.append(victor)
        i += 1
    return pair

# tournament function, the lowest fitness wins  
def tournament(a, b):
    if float(a[1]) > float(b[1]):
        return a
    else:
        return b

# crossover function mates the two tournament victors
def crossover(pair):
    newMember = []
    a = pair[0]
    b = pair[1]
    gene1 = a[0]
    gene2 = b[0]
    # the crossover point is randomly selected
    num = random.randrange(0,1)
    if num == 0:
        newMember.extend([gene1[0],gene2[1]])
    if num == 1:
        newMember.extend([gene1[1],gene2[0]])
    return newMember

# a newGene is randomly applied and created
def mutate(member, mutationRate):
    newGene = 0
    num = random.uniform(0, 1)
    if float(num >= mutationRate):
        newGene = round(random.uniform(0.5, 5), 2)
        #the placement within the newMember is randomly selected
        if num > 0.75: #needs to be dynamic
            del member[1]           
            member.append(newGene)
        else:
            del member[0]
            member.insert(0, newGene)
    return member
  
#main method
def main(popSize, numOfIterations, mutationRate):
    print('--------------------')
    print('Creating Population')
    print('--------------------')
    bestFitness = []
    fitnessArray = []
    fitness = 0
    #initialise population
    pop = createNewPop(popSize)     
    fitnessArray = createFitnessArray(pop, popSize, fitness)
    #fitnessArray = [[[1.77, 0.9], 0.55],[[4.54, 0.9], 0.55], [[4.54, 0.9], 0.5], [[1.77, 1.6], 0.38], [[1.77, 1.6], 0.38], [[4.66, 1.6], 0.35], [[0.83, 2.55], 0.33], [[4.66, 1.6], 0.33], [[4.66, 1.6], 0.33], [[1.77, 2.55], 0.3]]
    #main loop
    print('--------------------')
    print('Starting Iterations')
    print('--------------------')
    i=0
    while i < numOfIterations:         
        crossoverPair = getTournamentPair(fitnessArray)
        newMember = crossover(crossoverPair) 
        newMember = mutate(newMember, mutationRate)
        
        del fitnessArray[-1]
        function = fitnessFunction.fitnessFunction(newMember)
        fitness = function.run()
        newArr = [newMember, fitness]        
        fitnessArray.append(newArr)
        fitnessArray = sort(fitnessArray)
        bestFitness = fitnessArray[0]
        for x in fitnessArray:
            print(x)
        print('--------------------')
        print('Count: ' + str(i)) 
        print('Best: ' + str(bestFitness))
        print('--------------------')      
        i+=1
    
    return bestFitness

# call main method and apply popSize and numOfIterations    
best = main(10, 100, 0.5)
print('--------------------')
print('Complete')
print('Best: '+str(best))
print('--------------------')

'''
    [[4.54, 0.9], 0.5]
[[0.83, 2.55], 0.33]
[[1.77, 2.98], 0.28]
[[4.66, 2.79], 0.25]
[[1.85, 4.21], 0.25]
[[3.81, 2.55], 0.23]
[[4.39, 3.06], 0.23]
[[4.66, 4.21], 0.2]
[[4.53, 4.91], 0.17]
[[4.54, 0.9], 0.08]
'''

