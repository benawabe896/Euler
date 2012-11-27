import sys
def isPrime(n):
	if n <= 1:
		return False
	for i in range(2,n):
		if n% i == 0: 
			return False
	return True

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

primes = getPrimes(100)

categories = {0:{},1:{},2:{},3:{},4:{},5:{}}

for p in primes:
	# iterate through the characters of the primes and assign them to 
	# the categories appropriately i.e.
	# 01 and 10 are the categories of two digits
	# 001 010 100 011 101 110 and the categories for three digits


