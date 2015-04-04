import math
from decimal import *

def load_triangles():
    file = open('p102_triangles.txt')
    #file = open('test_file.txt')
    triangles = []
    for line in file:
        points = line[:-1].split(',')
        triangles.append(points)
    return triangles

def x_intercepts((a,b),(c,d)):
    if (d - b) == 0:
        return None 
    if (c - a) == 0:
        if b*d <=0:
            return a
        else: 
            return None
    m = Decimal(d - b)/Decimal(c - a)
    if m == 0:
        return None
    if b*d<=0:
        return Decimal(m*a-b)/Decimal(m)
    return None

def y_intercepts((a,b),(c,d)):
    if (c - a) == 0:
        return None

    m = Decimal(d - b)/Decimal(c - a) 
    if m == 0:
        if a*c<=0:
            return b 
        else:
            return None
    if a*c<=0:
        return b-m*a
    return None

def origin_test((x,y),(s,t),(u,v)):
    x_points = sorted([x,s,u])
    y_points = sorted([y,t,v])
    left_wall = Decimal(x_points[0])
    if left_wall >= 0:
        return False 
    right_wall = Decimal(x_points[2])
    if right_wall <= 0:
        return False 
    top_wall = Decimal(y_points[2])
    if top_wall <= 0:
        return False
    bottom_wall = Decimal(y_points[0])
    if bottom_wall >= 0:
        return False
    # triangle pssibly contains origin
    x_int0 = x_intercepts((x,y),(s,t))
    x_int1 = x_intercepts((x,y),(u,v))
    x_int2 = x_intercepts((s,t),(u,v))
    y_int0 = y_intercepts((x,y),(s,t))
    y_int1 = y_intercepts((x,y),(u,v))
    y_int2 = y_intercepts((s,t),(u,v))
    exes = set()
    whys = set()
    if bottom_wall <= y_int0 <= top_wall:
        whys.add(y_int0)
    if bottom_wall <= y_int1 <= top_wall:
        whys.add(y_int1)
    if bottom_wall <= y_int2 <= top_wall:
        whys.add(y_int2)

    if left_wall <= x_int0 <= right_wall:
        exes.add(x_int0)
    if left_wall <= x_int1 <= right_wall:
        exes.add(x_int1)
    if left_wall <= x_int2 <= right_wall:
        exes.add(x_int2)
    exes.discard(None)
    whys.discard(None)
    if len(exes) == 1:
        return False
    if len(whys) == 1:
        return False
    if exes.pop()*exes.pop() < 0 and whys.pop()*whys.pop() < 0:
        return True
    return False

triangles = load_triangles()
count = 0
pos = 1
for triangle in triangles:
    pos+=1
    if origin_test((int(triangle[0]),int(triangle[1])),(int(triangle[2]),int(triangle[3])),(int(triangle[4]),int(triangle[5]))):
        count +=1
    else:
        pass

print "count: ",count
