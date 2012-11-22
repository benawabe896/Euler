"""
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 212
15 = 7 + 222
21 = 3 + 232
25 = 7 + 232
27 = 19 + 222
33 = 31 + 212

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""
import math, sys
from bisect import bisect_left

squares = {}
primes = {}
sumtwices = {}

for x in range(0,10):
	squares[x**2] = True
	
def getPrimes(n): 
	if n==2: return [2]
	elif n<2: return []
	s=range(3,n+1,2)
	mroot = n ** 0.5
	half=(n+1)/2-1
	i=0
	m=3
	while m <= mroot:
		if s[i]:
			j=(m*m-3)/2
			s[j]=0
			while j<half:
				s[j]=0
				j+=m
		i=i+1
		m=2*i+3
	return [2]+[x for x in s if x]

def isPrime(n):
	if n <= 1:
		return False
	for i in range(2,n):
		if n% i == 0: 
			return False
	return True

for x in getPrimes(100):
	for y in squares:
		sumtwice = x+2*y
		if sumtwice & 1 and True or False:
			if not isPrime(sumtwice):
				sumtwices[x+2*y] = True

for x in xrange(9,10000,2):
	if isPrime(x):
		continue
	isSumOfPrime = False
	for y in range(1,50):
		square = y**2
		if square > x:
			break
		leftover = x - 2*square
		if isPrime(leftover):
			isSumOfPrime = True
			break
	if not isSumOfPrime:
		print x
		sys.exit()
