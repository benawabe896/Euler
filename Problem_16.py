"""215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?"""

import time, math
ti = time.time()

total = 0
for ch in str(2**1000):
    total += int(ch)
print total
print "Time taken(secs):", time.time() - ti
