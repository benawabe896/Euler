"""The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""

squares = 0
sos = 0
maxi = 101
for i in range(1,maxi):
    squares += (i * i)
    sos += i
print squares
print sos
sos *= sos
print sos
print sos - squares
