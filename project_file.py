import random
PSize = 20
CourseS = ['C1', 'C2', 'C3', 'C4', 'C5']
E_HallS = ['H1', 'H2']
T_SlotS = ['T1', 'T2', 'T3']
PArr = []
SizeTourn= 5
bestFitArray =[]
class C_Fitness:
    def __init__(self, Res):
        #variable to store the schedule
        self.Res = Res
        
        #print(self.Res)
    def calculate_fitness(self):
        #variable to store fitness count
        CalculateFCount = 0
        #variable to store count of exams in hall 1
        #variable to store count of exams in hall 2
        H1Count = 0 
        H2Count = 0
        C1C4 = 5
        C1C2= 10
        C2C5= 7
        C4C5= 8
        C3C4= 12
        conflict = 10
        #calculate fitness count for each exam in chromosome 
        
        for vari, iEx in enumerate(self.Res):
            if iEx[1] == 'H1' :
                    H1Count+=1
            elif iEx[1] == 'H2' :
                    H2Count+=1
            for vark, kEx in enumerate(self.Res):
                
                # avoid comparing the same exam
                if vari != vark and vari < vark:  # Skip comparison with itself and compare only once
                    # Check if exams conflict in same hall and time slot 
                    if iEx[1] == kEx[1] and iEx[2] == kEx[2]:
                        #print(iEx, kEx)
                        if iEx[0]=='C1' and kEx[0]=='C2': #if courses are C1 and C2
                            CalculateFCount = (C1C2*100)+ conflict +CalculateFCount
                        #    print("conflict hall wala aa raha hai and time both")
                        #    print(CalculateFCount)
                        elif iEx[0]=='C1' and kEx[0]=='C4': #if courses are C1 and C4
                        #    print("conflict hall wala aa raha hai and time both")
                        #    print(CalculateFCount)
                            CalculateFCount = (C1C4*100) + conflict+CalculateFCount
                        elif iEx[0]=='C2' and kEx[0]=='C5': #if courses are C2 and C5
                        #    print("conflict hall wala aa raha hai and time both")
                        ##    print(CalculateFCount)
                            CalculateFCount = (C2C5*100) + conflict+CalculateFCount
                        elif iEx[0]=='C3' and kEx[0]=='C4': #if courses are C3 and C4
                          #  print("conflict hall wala aa raha hai and time both")
                          #  print(CalculateFCount)
                            CalculateFCount = (C3C4*100) + conflict+CalculateFCount
                        elif iEx[0]=='C4' and kEx[0]=='C5': #if courses are C4 and C5
                          #  print("conflict hall wala aa raha hai and time both")
                          #  print(CalculateFCount)
                            CalculateFCount = (C4C5*100) + conflict+CalculateFCount
                    # Check if exams conflict in different halls and same time slot
                    elif iEx[2] == kEx[2] and iEx[1] != kEx[1]: 
                        #print(iEx, kEx)
                        #print(iEx[0], kEx[0])
                        if iEx[0]=='C1' and kEx[0]=='C2': #if courses are C1 and C2
                           # print(iEx[0], kEx[0])
                          #  print("conflict time wala aa raha hai")
                          #  print(CalculateFCount)
                            CalculateFCount = (C1C2*100) +CalculateFCount
                        elif iEx[0]=='C1' and kEx[0]=='C4': #if courses are C1 and C4
                            #print(iEx[0], kEx[0])
                           # print("conflict time wala aa raha hai")
                           # print(CalculateFCount)
                            CalculateFCount = (C1C4*100)  +CalculateFCount
                        elif iEx[0]=='C2' and kEx[0]=='C5': #if courses are C2 and C5
                            #print(iEx[0], kEx[0])
                           # print("conflict time wala aa raha hai")
                           # print(CalculateFCount)
                            CalculateFCount = (C2C5*100) +CalculateFCount
                            #print(iEx[0], kEx[0])
                        elif iEx[0]=='C3' and kEx[0]=='C4': #if courses are C3 and C4
                           # print("conflict time wala aa raha hai")
                           # print(CalculateFCount)
                            CalculateFCount = (C3C4*100) +CalculateFCount
                        elif iEx[0]=='C4' and kEx[0]=='C5': #if courses are C4 and C5
                            #print(iEx[0], kEx[0])
                           # print("conflict time wala aa raha hai")
                            #print(CalculateFCount)
                            CalculateFCount = (C4C5*100)+CalculateFCount
        #print("hall 1 count")
        #print(H1Count)
        #print("hall 2 count")
        #print(H2Count)
        if H1Count > 3:
            CalculateFCount =  CalculateFCount +  (H1Count-3)*10
        elif H2Count > 3:
            CalculateFCount = CalculateFCount +  (H2Count-3)*10
        return CalculateFCount
def TournSelectt(subgro, fitne, size):
    print("subgroupss")
    print(subgro)
    print("Fitness of subgroupss")
    print(fitne)
    print("size of subgroupss")
    print(size)
    # returns the chromosome with the highest fitness
    
    selectedd = None
    best_fitness = float('inf') #negative infinity 
    for loopI in range(size): #loop through the subgroup
        if fitne[loopI] < best_fitness: #if fitness of subgroup is greater than best fitness
            selectedd = subgro[loopI] #select the subgroup
            best_fitness = fitne[loopI]#update best fitness
    print("Selected: ")
    print(selectedd)
    bestFitArray.append(best_fitness)
    print("Best Fitness: ")
    print(bestFitArray)
    return selectedd
# crossover function
def crossover(P1, P2):
    # select a random crossover point
    # the crossover point should not be the first or last index
    # because we need to keep at least one gene from each parent
    # the crossover point should be an integer
    # the crossover point should be less than the length of the parent chromosomes
    # the crossover point should be greater than 0
    ValR = random.random()
    if (ValR < 0.8):
        return None, None, None
    PCrover = random.randint(1, len(P1) - 1)
    
    # create two empty offspring chromosomes
    # the offspring chromosomes will be the same length as the parents
    # the offspring chromosomes will be lists
    # the offspring chromosomes will contain the same data type as the parents
    offspring1 = []
    offspring2 = []
    
    # swap genetic information between parents at the crossover point
    # the genetic information before the crossover point will be taken from parent1
    # after the crossover point will be taken from parent2
    # for 2nd child bfr the crossover point will be taken from parent2
    # afr crossover point will be taken from parent1
    # genetic info before the crossover point will be added to child1
    # after the crossover point will be added to child1
    # genetic info bfr the crossover point will be added to 1stchild
    # the genetic information after the crossover point will be added to 2ndchild
    # the offspring chromosomes will be returned
    # the offspring chromosomes will be lists
    offspring1 = P1[:PCrover] + P2[PCrover:]
    offspring2 = P2[:PCrover] + P1[PCrover:]
    
    # return the two offspring chromosomes
    return offspring1, offspring2 , PCrover 
# choose a random gene to mutate
# randomly choose a new value for the gene
# return the mutated chromosome
# choose a random gene to mutate 
def mutation(individual): #mutate a random gene in the chromosome
    ValR = random.random()
    if (ValR < 0.1):
        return False, None
    tempM = individual.copy() #copy the chromosome
   
    randM = random.randint(0, len(tempM)-1) 
    
    # we randomly chose New value for the geene
    new_value = [CourseS[randM],random.choice(E_HallS), random.choice(T_SlotS)]
    tempM[randM]=new_value
    print("Mutated chromosome: ")
    print(tempM)
    return True, tempM        
if __name__ == "__main__":
 
    for var in range(PSize):
        ChromosomeArr = []
        for varC in CourseS:
            #variable to store the schedule
            SchedArr = []
            #append course to schedule
            SchedArr.append(varC)
            #randomly select hall
            EhallRand = random.choice(E_HallS)
            #append hall to schedule
            SchedArr.append(EhallRand)
            #randomly select time slot
            TslotRand = random.choice(T_SlotS)
            #append time slot to schedule
            SchedArr.append(TslotRand)
            #append schedule to chromosome
            ChromosomeArr.append(SchedArr)
            
        print("Schedules: " + str(ChromosomeArr))
        #append chromosome to population
        PArr.append(ChromosomeArr)
    #print(PArr)
    bestFit = []
    for generation in range(0, 100):
        fitnessArr = []
        for finess in PArr:
            fit = C_Fitness(finess).calculate_fitness()
            fitnessArr.append(fit)
        bestC= PArr[fitnessArr.index(min(fitnessArr))]
        bestFit.append(bestC)
        if(min(fitnessArr)==0):
            
            print("\n\n\n")
            print("BREAKING THE LOOP")
            print("\n\n\n")
            break
    print("bestFit")
    print(bestFit)  
    Subgrouping = [PArr[i:i + SizeTourn] for i in range(0, len(PArr), SizeTourn)]
    tourn= []
    for Sub in Subgrouping:
        Sfit = [fitnessArr[PArr.index(i)] for i in Sub]
        tourn.append(TournSelectt(Sub, Sfit, SizeTourn))
    PopN= tourn[:4]

    print("PopN")
    print(PopN)
    popSize = len(PopN)
    #parents = TournSelectt(PArr, selected,SizeTourn)
    childd = []
    for loop in range(0,len(PopN),2):
        # crossover
        oSpr1,oSpr2,crossO = crossover(PopN[loop], PopN[loop+1])
        #childd.append(offspring)
        if(oSpr1 == None or oSpr2 == None or crossO== None):
            print("Can't do crossover")
        else:
            VarF1 = C_Fitness(oSpr1).calculate_fitness()
            PopN.append(oSpr1)
            bestFitArray.append(VarF1)
            
            VarF2 = C_Fitness(oSpr2).calculate_fitness()
            PopN.append(oSpr2)
            bestFitArray.append(VarF2)
            print("\n\n")
            print("Original Parents:\n", PopN[loop], PopN[loop+1])
            print("\n\n")
            print("crossover childs:\n", oSpr1, oSpr2)
            print("\n\n")
            
            
            popSize= popSize+2
    for loop in range(len(PopN)):
    # mutation
        mutated, tempM = mutation(PopN[loop])
        if mutated:
            VarF = C_Fitness(tempM).calculate_fitness()
            PopN.append(tempM)
            bestFitArray.append(VarF)
            popSize= popSize+1
        else:
            print("Can't do mutation")
            
            
    print("\n\n\n")
    print("PopN")
    print(PopN)
    print("bestFitArray")
    print(bestFitArray)
    print("PSize")
    print(popSize)
    print("\n\n\n")

        
        
        

    