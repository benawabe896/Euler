"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""

import math, sys, itertools

def isPrime(n):
	if n <= 1:
		return False
	for i in range(2,n):
		if n% i == 0: 
			return False
	return True

def getPrimePermutations(arr):
	primes = []
	for x in itertools.permutations(arr):
		permute = int(''.join(str(elem) for elem in x))
		if isPrime(permute):
			primes.append(permute)
	return sorted(primes)

def getSimilarDiffs(arr):
	diffs = {}
	candidates = []
	for x in arr:
		for y in arr:
			if y > x:
				diff = y-x
				if diff in diffs:
					if diffs[diff][1] == x:
						candidates.append(diffs[diff])
						candidates.append((x,y,diff))
				diffs[y-x] = (x,y,diff)
	return candidates

for x in xrange(1234,9876):
	x = str(x)
	#if len(list(x)) == len(set(list(x))):
	primePermutes = getPrimePermutations(str(x))
	simDiffs = getSimilarDiffs(primePermutes)
	if len(simDiffs):
		print simDiffs
