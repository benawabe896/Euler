"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""


def isprime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return True    
    # all other even numbers are not primes
    if not n & 1: 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

def primes(n):
  """ returns a list of prime numbers from 2 to < n """
  if n < 2:  return []
  if n == 2: return [2]
  # do only odd numbers starting at 3
  s = range(3, n, 2)
  # n**0.5 may be slightly faster than math.sqrt(n)
  mroot = n ** 0.5
  half = len(s)
  i = 0
  m = 3
  while m <= mroot:
    if s[i]:
      j = (m * m - 3)//2
      s[j] = 0
      while j < half:
        s[j] = 0
        j += m
    i = i + 1
    m = 2 * i + 3
  # make exception for 2
  return [2]+[x for x in s if x]

"""
grand_total = 0 
for i in range(2,1000):
    if isprime(i):
        grand_total += i
print grand_total"""

primeList = primes(2000000)
#print primeList
print sum(primeList)


