"""The following iterative sequence is defined for the set of positive integers:

n  n/2 (n is even)
n  3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13  40  20  10  5  16  8  4  2  1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million."""

import time

def even(n):
    return n / 2

def odd(n):
    return (3 * n) + 1
    
ti = time.time()

longest_chain = 0
longest_start = 0
upper_bound = 1000000
chain_hash = {}

for i in range(upper_bound / 2, upper_bound):
    incr = i
    chain = []
    while incr > 0:
        if incr in chain_hash:
            chain_length = len(chain) + chain_hash[incr]
            chain_hash[i] = chain_length
            incr = 0
        else:
            chain.append(incr)
            if incr % 2 == 0:
                incr = even(incr)
            else:
                incr = odd(incr)
            if incr == 1:
                chain.append(1)
                chain_length = len(chain)
                chain_hash[i] = chain_length
                incr = 0
    if chain_length > longest_chain:
        longest_chain = chain_length
        longest_start = i
print "longest chain %d start %d" % (longest_chain, longest_start)    
print "Time taken(secs):", time.time() - ti
