"""A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""

import sys
import math

num = 1000
max_incr = 1000

for x in range(max_incr):
    for y in range(x + 1, max_incr):
        z = int(math.sqrt(x*x + y*y))
        if (x*x + y*y == z*z) and (x < y and y < z) and x + y + z == 1000:
            print "both " + str(x) + " " + str(y) + " "  + str(z)
            sys.exit()

"""Without programming: 

a= 2mn; b= m^2 -n^2; c= m^2 + n^2; 
a + b + c = 1000; 

2mn + (m^2 -n^2) + (m^2 + n^2) = 1000; 
2mn + 2m^2 = 1000; 
2m(m+n) = 1000; 
m(m+n) = 500; 

m>n; 

m= 20; n= 5; 

a= 200; b= 375; c= 425;"""
