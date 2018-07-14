from sympy import *
from sympy.combinatorics.subsets import ksubsets
from time import *

start = time()

prime = 11

found = False
while not found:
    digits = list(str(prime))
    positions = list(list(ksubsets(range(len(digits) - 1), k)) for k in range(1, len(digits)))
    positions = [item for sublist in positions for item in sublist]
    result = 10 ** 10
    for pos in positions:
        if pos[0] == 0:
            interval = range(1, 10)
        else:
            interval = range(10)
        n = 0
        min_prime = 10 ** 10
        for i in interval:
            new_digits = list(digits)
            for p in pos:
                new_digits[p] = str(i)
            new_number = int(''.join(d for d in new_digits))
            if isprime(new_number):
                n += 1
                if new_number < min_prime:
                    min_prime = new_number
                    print min_prime, time() - start
        if n == 8:
            if min_prime < result:
                result = min_prime
            found = True
    if found:
        print result
    prime = nextprime(prime)

end = time()
print end - start