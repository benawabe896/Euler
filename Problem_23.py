"""A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers."""

import time, math
ti = time.time()

def isabundant(n):
    divisors = [1]
    topbound = int(math.ceil(math.sqrt(n)))
    for i in range(2,topbound):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n / i)
    if math.sqrt(n) == topbound:
        divisors.append(topbound)
    if sum(divisors) > n:
        return True
    else:
        return False

top = 28124
abundants = []
abundant_sums = {}

for i in range(2, top):
    if isabundant(i):
        abundants.append(i)
        for ab in abundants:
            abundant_sums[i + ab] = True

notable = []
for i in range(1,top):
    if i not in abundant_sums:
        notable.append(i)

print sum(notable)



print "Time taken(secs):", time.time() - ti
