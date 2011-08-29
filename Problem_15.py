"""Starting in the top left corner of a 22 grid, there are 6 routes (without backtracking) to the bottom right corner.

How many routes are there through a 2020 grid?"""

import time, math
ti = time.time()

"""
width = 5
height = 5

def recurse(width, height, end_width, end_height):
    if width == end_width and height == end_height:
        return 1
    w = 0
    h = 0
    if width < end_width:
        w = recurse(width + 1, height, end_width, end_height)
    if height < end_height:
        h = recurse(width, height + 1, end_width, end_height)
    return w + h
print recurse(0, 0, width, height)
"""

def binomialCoefficient(n, k):
    if k > n - k: # take advantage of symmetry
        k = n - k
    c = 1
    for i in range(k):
        c = c * (n - i)
        c = c / (i + 1)
    return c

print binomialCoefficient(40,20)

"""
a = 20
b = math.factorial(a)

print math.factorial(2 * a) / (b * b)
"""
print "Time taken(secs):", time.time() - ti
