validSet = set(str(i) for i in xrange(1,10))
count = 0
count2 = 0
solutionSet = [line.split()for line in open('file.txt')]
#solutionSet = [line.split()for line in open('results.txt')]
for solution in solutionSet:
    print solution    
    for row in solution:
        if len(set(row)) == len(validSet):
            count+=1
    for i in range(len(solution)):
        print set(row[i] for row in solution)
        if len(set(row[i] for row in solution))==len(validSet):
            count2+=1
