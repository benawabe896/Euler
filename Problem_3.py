"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""

largest = 600851475147
factors = []

def recurse(largest):
    incr = 2
    while incr < largest / 2:
        if largest % incr == 0:
            factors.append(incr)
            return recurse(largest / incr)
        incr += 1
    factors.append(largest) # the last 
recurse(largest)
print factors

