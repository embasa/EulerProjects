
def amicable(num):
    return sum( i for i in xrange(1,num/2+1) if (num%i==0) )

print sum( n for n in range(10000) if ( amicable( amicable(n) )==n ) and (amicable(n)!=n) )


