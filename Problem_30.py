"""Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits."""

import time

ti = time.time()

total = 0
for x in range(2,1000000):
    allnums = 0
    for ch in str(x):
        allnums += int(ch)**5
    if x == allnums:
        print x
        total += x

print total
print "Time taken(secs):", time.time() - ti
