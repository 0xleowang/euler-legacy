# Theorem: Every number n can at most have one prime factor greater than sqrt(n).

from math import sqrt

n = 600851475143
if n % 2 == 0:
    lastFactor = 2
    n /= 2
    while n % 2 == 0:
        n /= 2
else:
    lastFactor = 1

factor = 3

maxFactor = sqrt(n)
while n > 1 and factor <= maxFactor:
    if n % factor == 0:
        n /= factor
        lastFactor = factor
        while n % factor == 0:
            n /= factor
        maxFactor = sqrt(n)
    factor = factor + 2

print lastFactor if n == 1 else n