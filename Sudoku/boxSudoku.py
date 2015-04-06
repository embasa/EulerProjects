from pyeda.inter import *
size = 3
box = [[[False for i in range(size)]for j in range(size)]for k in range(size)]


for k in range(size):
    for j in range(size):
        print box[k][j], '\t',
    print ''
