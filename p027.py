"""
Euler discovered the remarkable quadratic formula:

n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
"""
import primeTest
primes = []
def quatric():
    prev_product = 0
    product = 0
    largest_count = -1
    count = 0
    for a in xrange(-1000,1000,1):
        for b in xrange(-1000,1000,1):
            i=0
            
            while primeTest.is_prime(i**2+a*i + b):
                count+=1
                i+=1
            if count > largest_count:
                largest_count = count
                product = a*b
            count = 0
    print product


quatric()

