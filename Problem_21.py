"""Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000."""

import time, math

def getproperdivisorssum(n):
    divisors = []
    topbound = int(math.sqrt(n))
    for i in range(1,topbound):
        if n % i == 0:
            divisors.append(i)
            if i != 1: #proper
                divisors.append(n / i)
    if math.sqrt(n) == topbound:
        divisors.append(topbound)
    return sum(divisors)


ti = time.time()

divisors = {}
total = 0
for i in range(2,10000):
    if i not in divisors:
        dsum = getproperdivisorssum(i)
        if dsum not in divisors:
            osum = getproperdivisorssum(dsum)
            if osum == i and i != dsum:
                print "%d => %d => %d" % (i, dsum, osum)
                total = total + i + dsum
                divisors[dsum] = True
                divisors[i] = True
print total
print "Time taken(secs):", time.time() - ti
