#hello
import sys
import itertools
import copy
#print len(permutations)
def populatePermutationsPerPosition(currentGame,columnValues,currentPermutations):
    permutationsPerPosition = []
    for row in currentGame:
        copyArray = copy.deepcopy(currentPermutations)
        #for every position it row, replace current list with one that meets the conditions, thus shortening it for future iterations
        for i in range(len(row)):
            copyArray = [permutation for permutation in copyArray if ((row[i] =='0') and (permutation[i] not in columnValues[i])) or (row[i] == permutation[i])]

        permutationsPerPosition.append(copyArray)
    return permutationsPerPosition


def generateColumnValuesForGame(newRow,columnValues):
    for i in range(len(columnValues)):
        columnValues[i].add(newRow[i])
    return columnValues

def testValue(value,columnValues):
    for i in range(len(value)):
        if value[i] in columnValues[i]:
            return True
    return True

def recursiveSolutionGenerator(currentGame,columnValues,currentPermutationsPerPosition,count):
    indexOfSmallest = -1
    smallestValue = sys.maxint 
    for i in xrange(0,len(currentGame)):
        if len(currentPermutationsPerPosition[i])>1 and len(currentPermutationsPerPosition[i]) < smallestValue:
            indexOfSmallest = i
            smallestValue = len(currentPermutationsPerPosition[i])

    print indexOfSmallest, [len(permutationsList) for permutationsList in currentPermutationsPerPosition],' ', #,' '.join([''.join(list(columnValues[x])) for x in range(9)])
    permutationsToTry = []
    if indexOfSmallest >= 0:
        permutationsToTry = currentPermutationsPerPosition[indexOfSmallest]
    else:
        return
#    print indexOfSmallest,smallestValue, permutationsToTry
    for value in permutationsToTry:
        currentGame[indexOfSmallest] = value
        
        copyOfColumnValues = [set([row[i] for row in currentGame if row[i] != '0']) for i in range(9)]
#        copyOfColumnValues# = generateColumnValuesForGame(value,copy.deepcopy(columnValues))
        print ' '.join([''.join(list(copyOfColumnValues[x])) for x in range(9)])

        currentPermutationsArray = populatePermutationsPerPosition(currentGame,copyOfColumnValues,list(set([x for p in currentPermutationsPerPosition for x in p])))
#    print indexOfSmallest,[len(permutationsList) for permutationsList in currentPermutationsArray]
        if all([len(permutationsList)>0 for permutationsList in currentPermutationsArray]):
            if  all([len(permutationsList)==1 for permutationsList in currentPermutationsArray]):
                count = True
                return currentPermutationsArray 
            result = recursiveSolutionGenerator(currentGame,copyOfColumnValues,currentPermutationsArray,count)
            if result is not None and all([len(permutationsList)==1 for permutationsList in result]):
                return result 
        else:
            return 
        #end of testValue if statement

#monkeyness.com

def mainLoop():
    permutations = [''.join(element) for element in itertools.permutations('123456789')]
    #trimmedInput = [line.rstrip() for line in open('p096_sudoku.txt')]
    trimmedInput = [line.rstrip() for line in open('one_game.txt')]
    games = [ row for row in trimmedInput if row[:4] != 'Grid']
    gameCount = len(games)/9
    total = 0
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print '\n'.join(games)
    print "*****************************************"
    for j in xrange(0,gameCount):
        currentGame = copy.deepcopy(games[j*9:9+j*9])
        column_values = [set([row[i] for row in currentGame if row[i] != '0']) for i in range(9)]
        print "j:",j
        print '\n'.join([' '.join(list(column_values[x])) for x in range(9)])
        print "--------------------------------------"
        permutationsPerPosition = populatePermutationsPerPosition(currentGame,column_values,permutations)
        
        originalCount = False 
        solution = recursiveSolutionGenerator(currentGame,column_values,permutationsPerPosition,originalCount)
        if solution is not None:
            sol = ""
            for val in solution:
                sol += val[0] + ' '
            print sol 
mainLoop()


