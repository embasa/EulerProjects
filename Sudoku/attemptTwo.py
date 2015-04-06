#attempt 2 at sudoku
import copy
COUNT = 0
fullHouse = set(['1','2','3','4','5','6','7','8','9'])
def subSquare(x,y,grId):
    for i in xrange(3*(x/3),3*(x/3)+3):
        for j in xrange(3*(y/3),3*(y/3)+3):
            if len(grId[i][j])>1:
                grId[i][j] = grId[i][j] - grId[x][y]

def solveGame(game):
    global COUNT
    grid = [[copy.deepcopy(fullHouse) for i in range(len(fullHouse))]for j in range(len(fullHouse))]
    for i in range(len(grid)):
        for j in range(len(grid)):
            if game[i][j] != '0':
                grid[i][j] = grid[i][j].intersection(game[i][j])

    solved = False 
    grid2 = [[]]

    while not solved:
        solved = True
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                if len(grid[i][j])==1:
                    count += 1
                    clearGrid(i,j,grid)
                elif len(grid[i][j]) == 0:
                    return False
                else:
                    solved = False
        if grid2 == grid:
            if count == 81:
                solved = True
            else:
                solved = False 
            break
        grid2 = copy.deepcopy(grid)
        
    if solved:
        COUNT +=1
        print "first",' '.join([''.join([list(element)[0]for element in row])for row in grid]) 
    #print ' '.join([''.join([list(element)[0]for element in row])for row in grid]) 
    else:
#        pass
        guessMethod(game,grid)
    return solved


def guessMethod(game,grid):
    print "FIRSTLIN!!!!!!"
    for row in game:
        print '        ','          '.join(row)
    print "--------------------------------------------------------------------------------------------------------------"
    for i in range(len(grid)):
        for j in range(len(grid)):
            print ''.join([val for val in grid[i][j]]).rjust(10),
        print ''
    x = -1
    y = -1
    smallestValue = 110
    copyGrid = copy.deepcopy(grid)
    for i in range(len(grid)):
        for j in range(len(grid)):
            if len(grid[i][j])>1 and len(grid[i][j]) < smallestValue :
                x = i
                y = j
                smallestValue = len(grid[i][j])
    print"beforeLoop:",x,y, grid[x][y]
    copyOfSet = copy.deepcopy(grid[x][y])
    secondCopyOfSet = copy.deepcopy(grid[x][y])
    solved = False 
    while len(secondCopyOfSet)>0 and not solved:
        grid = copy.deepcopy(copyGrid)
        grid[x][y] = set(secondCopyOfSet.pop())
        grid2 = [[]]
        print grid[x][y]
        while not solved:
            solved = True
            count = 0
            for i in range(len(grid)):
                for j in range(len(grid)):
                    if len(grid[i][j])==1:
                        count += 1
                        clearGrid(i,j,grid)
                    elif len(grid[i][j]) == 0:
                        print "ASFSDFSDF"
                        pass                    
                    else:
                        solved = False
            print '***********************************************************************************************************'                
            for i in range(len(grid)):
                for j in range(len(grid)):
                    print ''.join([val for val in grid[i][j]]).rjust(10),
                print ''
            if grid2 == grid:
                if count == 81:
                    print"solved2", ' '.join([''.join([list(element)[0]for element in row])for row in grid]) 
                    solved = True
                else:
                    solved = False 
                break
            grid2 = copy.deepcopy(grid)
        #print"solved", ' '.join([''.join([list(element)[0]for element in row])for row in grid]) 

def clearGrid(x,y,gRid):
    if len(gRid[x][y]) == 1:
        for i in range(len(gRid)):
            if len(gRid[x][i]) >1:
                gRid[x][i] = gRid[x][i] - gRid[x][y]
                
        for j in range(len(gRid)):
            if len(gRid[j][y]) >1:
                gRid[j][y] = gRid[j][y] - gRid[x][y]
        subSquare(x,y,gRid)

games = [line.rsplit() for line in open('p096_sudoku.txt') if line[:4] !='Grid']
games = [line for row in games for line in row]
gameCount = len(games)/9
for i in range(gameCount):
    solveGame(games[i*9:i*9+9])
