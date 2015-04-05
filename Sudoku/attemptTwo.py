#attempt 2 at sudoku
import copy
fullHouse = set(['1','2','3','4','5','6','7','8','9'])
def subSquare(x,y,grId):
#    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    for i in xrange(3*(x/3),3*(x/3)+3):
        for j in xrange(3*(y/3),3*(y/3)+3):
            if len(grId[i][j])>1:
                grId[i][j] = grId[i][j] - grId[x][y]
 #           print repr(int(''.join(grId[i][j]))).rjust(9),
  #      print '\n'
   # print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

def clearGrid(x,y,gRid):
    #print ''.join(gRid[x][y]),
    if len(gRid[x][y]) == 1:
        for i in range(len(gRid)):
            if len(gRid[x][i]) >1:
                gRid[x][i] = gRid[x][i] - gRid[x][y]
                
        for j in range(len(gRid)):
            if len(gRid[j][y]) >1:
                gRid[j][y] = gRid[j][y] - gRid[x][y]
        subSquare(x,y,gRid)

game =[ line.rsplit() for line in open('mike.txt')]
game = [line for row in game for line in row]
grid = [[copy.deepcopy(fullHouse) for i in range(len(fullHouse))]for j in range(len(fullHouse))]

print "---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+--"
for i in range(len(grid)):
    for j in range(len(grid)):
        val = copy.deepcopy(fullHouse)
        if game[i][j] != '0':
            grid[i][j] = grid[i][j].intersection(game[i][j])
        print repr(int(''.join(grid[i][j]))).rjust(9),
    print '\n'
print "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&"

for i in range(len(grid)):
    for j in range(len(grid)):
        if len(grid[i][j])==1:
            clearGrid(i,j,grid)
            break
        else:
            pass
#            print '0',

for i in range(len(grid)):
    for j in range(len(grid)):
        val = copy.deepcopy(fullHouse)
        if game[i][j] != '0':
            grid[i][j] = grid[i][j].intersection(game[i][j])
        print repr(int(''.join(grid[i][j]))).rjust(9),
    print '\n'

