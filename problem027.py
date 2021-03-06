#!/usr/bin/python3
#
# Project Euler (projecteuler.net) - Problem 27
# Euler published the remarkable quadratic formula:
#
# n² + n + 41
#
# It turns out that the formula will produce 40 primes for the consecutive 
# values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is
# divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly 
# divisible by 41.
#
# Using computers, the incredible formula  n²  79n + 1601 was discovered, 
# which produces 80 primes for the consecutive values n = 0 to 79. The product
#  of the coefficients, 79 and 1601, is 126479.
#
# Considering quadratics of the form:
#
# n² + an + b, where |a|  1000 and |b|  1000
#
# where |n| is the modulus/absolute value of n
# e.g. |11| = 11 and |4| = 4
# Find the product of the coefficients, a and b, for the quadratic expression 
# that produces the maximum number of primes for consecutive values of n, 
# starting with n = 0.

def isprime(n):
    n = abs(int(n))
    if n < 2: return False
    if n == 2: return True    
    if not n & 1: return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

def q(n,a,b):
    return n**2 + a*n + b

s = 1000
max = ma = mb = 0
for a in range( -s, s+1 ):
    for b in range( -s, s+1 ):
        n = 0
        while 1:
            if not isprime(q(n,a,b)): break
            n += 1
        if n > max: max, ma, mb = n, a, b

print( ma * mb )
