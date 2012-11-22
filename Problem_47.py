"""
The first two consecutive numbers to have two distinct prime factors are:
14 = 2  7
15 = 3  5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2**2  7  23
645 = 3  5  43
646 = 2  17  19.

Find the first four consecutive integers to have four distinct primes factors. What is the first of these numbers?
"""

import math, sys

def factorize(n):
   if n < -1: return [(-1, 1)] + factorize(-n)
   elif n == -1: return [(-1, 1)]
   elif n == 0: return [(0, 1)]
   elif n == 1: return [(1, 1)]
   else:
      def factor_out(n, divisor):
         power = 0
         while (n % divisor) == 0:
            n //= divisor
            power += 1
         return (n, power)
      factors = []
      sqrtn = math.sqrt(n)
      for divisor in (2, 3, 5):
         if divisor > sqrtn:
            break;
         n, power = factor_out(n, divisor)
         if power > 0:
            factors.append((divisor, power))
            sqrtn = math.sqrt(n)
      divisor_group = 0
      while divisor_group < sqrtn:
         for divisor_index in (7, 11, 13, 17, 19, 23, 29, 31):
            divisor = divisor_group + divisor_index
            if divisor > sqrtn:
               break;
            n, power = factor_out(n, divisor)
            if power > 0:
               factors.append((divisor, power))
               sqrtn = math.sqrt(n)
         divisor_group += 30
      if n > 1:
         factors.append((n, 1))
      return factors

def divisors_from_factors(factors):
   def unsorted_divisors_from_factors(factors):
      if not factors: return [1]
      else:
         base, max_power = factors[0]
         if base == -1: return unsorted_divisors_from_factors(factors[1:])
         elif base == 0: return []
         elif base == 1: return unsorted_divisors_from_factors(factors[1:])
         else:
            divisors = unsorted_divisors_from_factors(factors[1:])
            all_divisors = []
            for power in xrange(0, max_power+1):
               all_divisors += map(lambda x: x * base ** power, divisors)
            return all_divisors
   all_divisors = unsorted_divisors_from_factors(factors)
   all_divisors.sort()
   return all_divisors


def run_factorize(n):
   def str_from_factors_exp(factors):
      def str_from_factor(factor):
         if factor[1] == 1: return str(factor[0])
         else: return "^".join(map(str, factor))
      return " * ".join(map(str_from_factor, factors))
   def str_from_factors_mul(factors):
      factors = map(lambda x: [x[0]] * x[1], factors)
      factors = reduce(lambda x,y: x + y, factors, [])
      return " * ".join(map(str, factors))
   def pairs_from_divisors(d):
      return map(lambda x: (d[x], d[len(d)-x-1]), xrange(0, (1 + len(d)) // 2))
   def str_from_pairs(pairs):
      pairs = map(lambda x: "*".join(map(str, x)), pairs)
      return "0*0" if not pairs else "\t".join(pairs)
   f = factorize(n)
   print str(n) + " = " + str_from_factors_exp(f)
   print str(n) + " = " + str_from_factors_mul(f)
   print
   d = divisors_from_factors(f)
   print "Divisors: " + ("N/A" if not d else ", ".join(map(str, d)))
   s = reduce(lambda x,y: x + y, d, 0)
   sn = s - abs(n)
   s2n = sn - abs(n)
   ss = "zero" if s == 0 else "unit" if sn == 0 else "prime" if sn == 1 else "deficient" if s2n < 0 else "perfect" if s2n == 0 else "abundant"
   print "sigma_0(n) = " + str(len(d))
   print "sigma_1(n) = " + str(s)
   print "sigma_1(n)-n = " + str(sn)
   print "sigma_1(n)-2n = " + str(s2n)
   print str(abs(n)) + " is " + ss + "."
   print
   p = pairs_from_divisors(d)
   print "Pairs:"
   print str_from_pairs(p)


for x in xrange(1,10000000):
	facts = factorize(x)
	factsm1 = factorize(x-1)
	factsm2 = factorize(x-2)
	factsm3 = factorize(x-3)
	if not facts or not factsm1 or not factsm2 or not factsm3:
		continue
	if len(facts) == 4 and len(factsm1) == 4 and len(factsm2) == 4 and len(factsm3) == 4:
		print x, x-1, x-2, x-3
		sys.exit()
