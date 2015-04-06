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
        print ' '.join([''.join([list(element)[0]for element in row])for row in grid]) 
    #print ' '.join([''.join([list(element)[0]for element in row])for row in grid]) 
    else:
        guessMethod(game,grid)
    return solved

def guessMethod(game,grid):
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
    print grid[x][y],smallestValue
    copyOfSet = copy.deepcopy(grid[x][y])
    print copyOfSet

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
