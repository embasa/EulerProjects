#problem 96 euler using solver from someone elses code
import solver

allRows = [line.rsplit() for line in open('p096_sudoku.txt')if line[:4] != 'Grid']
count = len(allRows)/9

print count
total = 0
for pos in range(count):
    #take 9 rows that correspond to a single game, parse into 9 int arrays;each array being a row of the puzzle
    grid = [[int(i) for j in row for i in j]for row in allRows[9*pos:9*pos+9]]
    if solver.solveSudoku(grid):
        num = grid[0][0]*100 + grid[0][1]*10 + grid[0][2]
        total += num

print grid
print total
