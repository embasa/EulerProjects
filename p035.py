import primeTest

i = 197           

limit = 1000000
def prime_array(num):
    s = str(num)
    copy = s
    array = []
    array.append(int(s))
    while copy != (s + s[0])[1:]:
        array.append(int((s+s[0])[1:]))
        s = (s + s[0])[1:] 
    return array

pos = 2
count = 0
while pos < limit: 
    a = []
    if primeTest.is_prime(pos):
       a = prime_array(pos) 
       if len({num for num in a if primeTest.is_prime(num)}) == len(a):
           count+=1
    pos+=1
    
print count
