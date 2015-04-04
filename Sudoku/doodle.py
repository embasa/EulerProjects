#monkeyness.com
import itertools
import copy
import sudoku
#loads game from file
# make sets fro the game 

def mainLoop():
    permutations = [''.join(element) for element in itertools.permutations('123456789')]
    trimmedInput = [line.rstrip() for line in open('p096_sudoku.txt')]
    #trimmedInput = [line[:-1] for line in open('one_game.txt')]
    games = [ row for row in trimmedInput if row[:4] != 'Grid']
    gameCount = len(games)/9
#    print '\n'.join(games) 
    total = 0
    for i in xrange(39,40):
        currentGame = copy.deepcopy(games[i*9:9+i*9])
        column_values = [set([row[i] for row in currentGame if row[i] != '0']) for i in range(9)]
        permutationsPerPosition = sudoku.populatePermutationsPerPosition(currentGame,column_values,permutations)
        
        originalCount = False 
        solution = sudoku.recursiveSolutionGenerator(currentGame,column_values,permutationsPerPosition,originalCount)
        print i, solution
        #total+= int(solution[0][0][:3]) 
mainLoop()
