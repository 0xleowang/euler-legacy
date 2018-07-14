from fractions import gcd
from time import time
from math import sqrt

start = time()

limit = 1500000
m = 2
n = 1
l = []
g = []
for m in range(2, int(sqrt(limit) / 2)):
    for m in range(n + 1, int((-n + sqrt(2 * limit + n * n)) / 2)):
        if m % 2 == 0 or n % 2 == 0:
            if gcd(m, n) == 1:
                i = 1
                num = 2 * m * (m + n)
                while i * num <= limit:
                    if i * num not in l:
                        l.append(i * num)
                        print i * num, len(l), len(g), time() - start
                    else:
                        if i * num not in g:
                            g.append(i * num)

end = time()

print l