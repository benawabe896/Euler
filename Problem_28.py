"""Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?


t=1 
for n=3 to 1001 Step 2 
t=t+4*n^2-6*n+6 
next n 
But other languages could support something like: 
int t=1; 
for (int n=3;n<=1001;n+=2) t+=4*pow(n,2)-6*n+6;

"""

import time

ti = time.time()

"""add 1"""
"""
3 5 7 9
13 17 21 25
31 37 43 49

"""

total = 1
n = 1
incr = 2
corners = 4
spiral = 1

while spiral < 1001:
    for i in range(1, corners + 1):
        n += incr
        print n
        total += n
    spiral += 2
    incr += 2

print total
print "Time taken(secs):", time.time() - ti
