#opens a file, reads first line from it. trims first and last characther, splits by pattern, sorts and assigns list to names
names = sorted(open('p022_names.txt').readline()[1:-1].split('","'))

#make list of namescore by summing name characters * (i+1), ten return that sum for final answer
print sum( sum( ord(char)-ord('A')+1 for char in names[i] )*(i+1) for i in range(len(names)))


