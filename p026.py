#do it
d_max = 0
d = 2
max_length = 0
count = 0
sequence = []
pattern = []
for d in xrange(2,1000):
    n = 1
    while n%d != 0 and n not in pattern and n!=0:
        pattern.append(n)
        sequence.append(n/d)
        if n/d == 0:
            n*=10
        else:
            n = n%d*10
    if n%d != 0:
        val =  len(''.join(str(i) for i in sequence)[sequence.index(int(n/d)):])
        if val > max_length:
            max_length = val
            d_max = d
        
    pattern = []
    sequence = []

print d_max
