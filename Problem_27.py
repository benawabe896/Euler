"""Euler published the remarkable quadratic formula:
n*n + n + 41
It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. Using computers, the incredible formula  n * n 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, 79 and 1601, is 126479.

Considering quadratics of the form:

n * n + an + b, where |a|  1000 and |b|  1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0."""

import time

ti = time.time()

def isprime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return True    
    # all other even numbers are not primes
    if not n & 1: 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

def consprimes(a,b):
    n = 0
    while n > -1:
        if not isprime(n*n + a*n + b):
            return n
        n += 1

def evalconsprimes(x,y):
    global top, top_x, top_y
    
    val = consprimes(x,y)
    if val > top:
        top_x = x
        top_y = y
        top = val
        
top = 0
top_x = 0
top_y = 0

for x in range(1,1000):
    for y in range(1,1000):
        print "%d %d" % (x,y)

        evalconsprimes(x,y)
        evalconsprimes(x * -1,y)
        evalconsprimes(x,y * -1)
        evalconsprimes(x * -1,y * -1)
        
print "%d %d %d" % (top, top_x, top_y)

print "Time taken(secs):", time.time() - ti
