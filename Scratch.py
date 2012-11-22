import math

"""
for n in range(10):
    print n * (n + 1)**2 / 2

for n in range(10):
    print n * (n + 2) * (2 * n - 1) / 8

strip = 100000
x = 100
n = strip - x
total = n
for i in range(1,x + 1):
     total *= (n + i)
total = total / math.factorial(x)
print total

for n in range(10):
    print n * (n + 1) / 2
"""

for n in range(10):
    print n * ( ( n / 4 + 3 / 8) * n - 1 / 4)

