"""
The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
"""

import math, sys

summ = 0
for x in range(1,1000):
	summ += x**x
print str(summ)[-10:]
