maxValue = 0
theP = 0
for p in range(3,1001):
    tri = set() 
    for i in range(1,p/2):
        a=i
        for j in range(1,p/2):
            b=j
            c=p-i-j
            if ((a+b)>c) and ((a**2+b**2)==c**2):
                tri.add(a)
                tri.add(b)
                tri.add(c)
    if len(tri)/3 > maxValue:
        maxValue = len(tri)/3
        theP = p
print theP
