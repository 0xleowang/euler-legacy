from itertools import permutations
from time import time

start = time()

SIZE = 5

rings = permutations(range(1, 2*SIZE+1))

results = set()

for ring in rings:
    external = ring[:SIZE]
    internal = ring[SIZE:]
    #
    solutions = []
    for i in range(SIZE):
        if i + 1 < SIZE:
            sol = (external[i], internal[i], internal[i+1])
        else:
            sol = (external[i], internal[i], internal[0])
        solutions.append(sol)
    #
    totals = map(sum, solutions)
    if totals.count(totals[0]) != SIZE:
        continue
    #
    min_external_sol = min(solutions)
    while solutions[0] != min_external_sol:
        solutions.append(solutions.pop(0))
    #
    digits = [i[n] for i in solutions for n in range(3)]
    result = int(''.join(map(str, digits)))
    #
    if len(str(result)) == 16:
        results = results.union([result])

    print result, time() - start

end = time()

print max(results), end - start