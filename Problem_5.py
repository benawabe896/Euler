"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

import sys

go = True
incr = 87297210
maxi = 20 * 19 * 18 * 17 * 16 * 15 * 14 * 13 * 12 * 11
maxi = 698377680

while incr <= maxi:
    print 'incr - ' + str(incr)
    match = True
    for i in range(11,20):
        if incr % i != 0:
            print 'i - ' + str(i)
            match = False
            break
    if match == True:
        print incr
        sys.exit()
    incr += 110

