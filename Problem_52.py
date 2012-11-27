import sys

for x in xrange(1,10000000):
	if sorted(set(str(x*2))) == sorted(set(str(x*3))) == sorted(set(str(x*4))) == sorted(set(str(x*5))) == sorted(set(str(x*6))):
		print x
		sys.exit()
