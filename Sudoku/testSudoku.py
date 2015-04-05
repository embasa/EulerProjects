validSet = set(str(i) for i in xrange(1,10))
print validSet
count = 0
count2 = 0
solutionSet = [line.split()for line in open('output.txt')]
for solution in solutionSet:
#    print solution    
    for row in solution:
        if set(row) == validSet:
            count+=1
    for i in range(len(solution)):
        if set(row[i] for row in solution):
            count2+=1
print count,count2
