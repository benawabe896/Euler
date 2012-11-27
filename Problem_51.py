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

primes = getPrimes(1000000)

categories = {1:{},2:{},3:{},4:{},5:{},6:{},7:{}}
for p in primes:
	if len(str(p)) < 5:
		continue
	# iterate through the characters of the primes and assign them to 
	# the categories appropriately i.e.
	# 01 and 10 are the categories of two digits
	# 001 010 100 011 101 110 and the categories for three digits
	for x in xrange(1,int(str(int("1"*len(str(p)))),2)):
		mask = str(bin(x)[2:]).zfill(20)
		newSt = list(str(p))

		prevX = ''
		for y in xrange(0,len(str(p))):
			incr = -1*(y+1)
			if mask[incr] == '1':
				if prevX == '':
					prevX = newSt[incr]
				if prevX != newSt[incr]:
					continue
				newSt[incr] = 'x'
		newSt = ''.join(newSt)
		lsp = len(str(p))
		currCat = categories[lsp]
		if newSt not in categories[lsp]:
			categories[lsp][newSt] = [] 
		if p not in  categories[lsp][newSt]:
			categories[lsp][newSt].append(p)

maxLen = 0
maxVal = ''
maxVals = ''
for lenn in categories:
	for newSt in sorted(categories[lenn]):
		vals = categories[lenn][newSt]
		if len(vals) == 8:
			maxVal = newSt
			maxLen = len(vals)
			maxVals = vals
			break
	
print maxVal, maxLen, maxVals

