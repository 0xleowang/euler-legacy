# http://mathworld.wolfram.com/Semiprime.html

from __future__ import division
from sympy import prime, primepi

n = 10 ** 8
s = 0
for k in range(1, primepi(sqrt(n)) + 1):
    s += primepi(n / prime(k)) - k + 1
print s