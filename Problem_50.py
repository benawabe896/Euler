"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""

import math, sys

def isPrime(n):
	if n <= 1:
		return False
	for i in range(2,n):
		if n% i == 0: 
			return False
	return True

def genPrimes(n): 
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

maxx = 1000000
primes = genPrimes(maxx)
lenPrimes = len(primes)
nums = 0
for seqLen in xrange(1000,1,-1):
	print 'new seqLen ', seqLen
	x = 0
	y = seqLen
	while y <= lenPrimes:
		nums += 1
		if nums % 1000 == 0:
			print nums

		block = primes[x:y]
		x += 1
		y += 1

		if sum(block) > maxx:
			break
		if sum(block) in primes:
			print block
			print sum(block)
			sys.exit() 
