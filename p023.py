

def binarySearch(find):
    low = 0
    high = len(abundant)-1
    while low <=high:
        mid = (low+high)/2
        if abundant[mid] > find:
            high = mid-1
        elif abundant[mid] < find:
            low = mid+1
        else:
            return True 
    return False

def div_sum(num):
    return sum( i for i in xrange(1,num/2+1) if (num%i==0) )

def test(num):
    pos = 0
    while abundant[pos] < num and pos < len(abundant):
        if binarySearch(num-abundant[pos]):
            return False
        pos+=1
    return  True

bound = 28123 #given in prompt
abundant =[ n for n in range(bound) if div_sum(n) > n ]
total = 0
for i in xrange(1,bound):
    if test(i):
        total += i

print total
