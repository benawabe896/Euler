"""A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d  1000 for which 1/d contains the longest recurring cycle in its decimal fraction part."""

import time, sys, math, string
from decimal import Decimal as D
from decimal import getcontext

getcontext().prec = 100 # working precision = 100 digits

ti = time.time()

longest_sequence = 0
for i in range(2,1001):
    whole = str(D(1) / D(i))[::-1]
    print whole
    cycle = ""
    for ch in whole:
        if ch in cycle:
            sequence = len(cycle) - string.find(cycle, ch)
            if sequence > longest_sequence:
                longest_sequence = sequence
            break
        cycle += ch
print longest_sequence
print "Time taken(secs):", time.time() - ti
