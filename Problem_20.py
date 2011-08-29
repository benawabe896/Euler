"""n! means n  (n  1)  ...  3  2  1

For example, 10! = 10  9  ...  3  2  1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!"""

import time, math


ti = time.time()

print sum([int(i) for i in str(math.factorial(100))])

print "Time taken(secs):", time.time() - ti
