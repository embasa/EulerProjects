#hello
import sys
import itertools
import copy
#print len(permutations)
def populatePermutationsPerPosition(currentGame,columnValues,currentPermutations):
    
    permutationsPerPosition = []
    for row in currentGame:
        #copy = currentPermutations #need a copy of all permutations for each row
        #copy = permutations
        copy = currentPermutations
        #for every position it row, replace current list with one that meets the conditions, thus shortening it for future iterations
        for i in range(len(row)):
            copy = [permutation for permutation in copy if ((row[i] =='0') and (permutation[i] not in columnValues[i])) or (row[i] == permutation[i])]
        permutationsPerPosition.append(copy)
    return permutationsPerPosition


def generateColumnValuesForGame(newRow,columnValues):
    for i in range(len(columnValues)):
        columnValues[i].add(newRow[i])
    return columnValues

def recursiveSolutionGenerator(currentGame,columnValues,currentPermutationsPerPosition,count):
    indexOfSmallest = -1#0 if  !=0 else 1
    smallestValue = sys.maxint 
    count = 0
    for i in range(len(currentGame)):
        if len(currentPermutationsPerPosition[i]) == 1:
            count+=1
    print indexOfSmallest,[len(permutationsList) for permutationsList in currentPermutationsPerPosition]
    for i in xrange(0,len(currentGame)):
        if len(currentPermutationsPerPosition[i])>1 and len(currentPermutationsPerPosition[i]) < smallestValue:
            indexOfSmallest = i
            smallestValue = len(currentPermutationsPerPosition[i])
    if count == 8:
        for i in range(len(currentGame)):
            if i != indexOfSmallest:
                print i,'|', ' '.join(currentPermutationsPerPosition[i][0])
            else:
                print i,'|', ' '.join('000000000')
    permutationsToTry = currentPermutationsPerPosition[indexOfSmallest]
    print indexOfSmallest,smallestValue
    for value in permutationsToTry:
        currentGame[indexOfSmallest] = value
        copyOfColumnValues = generateColumnValuesForGame(value,copy.deepcopy(columnValues))
        currentPermutationsArray = populatePermutationsPerPosition(currentGame,copyOfColumnValues,list(set([x for p in currentPermutationsPerPosition for x in p])))
        print indexOfSmallest,[len(permutationsList) for permutationsList in currentPermutationsArray]
        if all([len(permutationsList)>0 for permutationsList in currentPermutationsArray]):
            if  all([len(permutationsList)==1 for permutationsList in currentPermutationsArray]):
                count = True
                return currentPermutationsArray 
            result = recursiveSolutionGenerator(currentGame,copyOfColumnValues,currentPermutationsArray,count)
            if result is not None and all([len(permutationsList)==1 for permutationsList in result]):
                return result 
        else:
            return 


