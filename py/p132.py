from sympy import *
from time import time

start = time()

p = 0
n = 0
result = 0
while n < 40:
    p = nextprime(p)
    if pow(10, 10**9, 9*p) == 1:
        n += 1
        result += p

print result, time() - start