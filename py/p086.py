from math import *
from time import time

start = time()

num_sols = 0
a = 0
while not num_sols > 1000000:
    a += 1
    for b in range(1, a + 1):
        for c in range(1, b + 1):
            path = sqrt((b + c) ** 2 + a ** 2)
            if int(path) == path:
                num_sols += 1
    print a, num_sols, time() - start

end = time()

print a, num_sols, end - start