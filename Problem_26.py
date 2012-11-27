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

def is_prime(n):
	if n <= 1:
		return False
	for i in range(2,n):
		if n% i == 0: 
			return False
	return True

n = 997   #starting prime closest to limit
for p in range(n, 1 ,-2):
    if not is_prime(p): continue
    c = 1
    while (pow(10, c) - 1) % p != 0:
        c += 1
    if (p-c) == 1: break
 
print "Answer to PE26 = ",p
sys.exit()



getcontext().prec = 100 # working precision = 100 digits

ti = time.time()

longest_sequence = 0
longest_whole = 0
longest_num = 0

for i in range(2,1001):
    whole = str(D(1) / D(i))
    print whole + " " + str(i)
    cycle = ""
    for ch in whole:
        if len(cycle) > 20:
            if cycle == cycle[::-1]:
                break
                
            if cycle[:4] == cycle[-4:]:
                sequence = len(cycle) - 4
                if sequence > longest_sequence:
                    longest_sequence = sequence
                    longest_whole = whole
                    longest_num = i
        cycle += ch
print longest_num
print longest_sequence
print longest_whole
print "Time taken(secs):", time.time() - ti
