#thomas feeds with vayne
i = 1
increment = 2
limit = 1001*1001
count = 0
array = []
while( i <= limit):
    array.append(i)
    count= (count+1)%4
    i+=increment
    if count == 0:
        increment +=2

print sum(array)
