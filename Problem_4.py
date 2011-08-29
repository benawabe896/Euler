"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91  99.

Find the largest palindrome made from the product of two 3-digit numbers."""

import sys

largest = 0

def evalreverse(a,b):
    test1 = a * b
    print str(test1) + ' ' + str(test1)[::-1]
    print a
    print b
    if str(test1) == str(test1)[::-1]:
        print 'match'
        print test1
        print a
        print b
        sys.exit()


for i in range(190):
    x = 999 - i

    for j in range(190):
        y = 999 - j
        evalreverse(x,y)
    

