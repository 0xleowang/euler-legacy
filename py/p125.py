from math import *
from time import time

start = time()

def cons_sqrt(a, b):
    a = a - 1
    return (b * (b + 1) * (2 * b + 1) - a * (a + 1) * (2 * a + 1)) / 6

def palindromic(num):
    return True if str(num) == str(num)[::-1] else False

LIMIT = 10 ** 8

upper = int(ceil(sqrt(LIMIT / 2)))

l = []
for b in range(2, upper):
    for a in range(1, b):
        num = cons_sqrt(a, b)
        if num < LIMIT and palindromic(num):
            l.append(num)
            print num, a, b, time() - start

end = time()

print "----"
print sum(set(l)), end - start, upper