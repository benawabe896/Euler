import sys, math
def binomial(n,k): return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))

summ = 0
for x in xrange(1,101):
	for y in xrange(x,101):
		if binomial(y,x) > 1000000:
			summ += 1
	
print summ
