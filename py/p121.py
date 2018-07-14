from itertools import combinations
from __future__ import division, ceil

def subsets(S, m=0):
    if not m: m = len(S)
    return set(combinations(S, m))

def allsols(n):
    sols = set()
    for i in range(n//2+1, n+1):
        sols = sols.union(subsets(range(1, n+1), i))
    return sols

n = 15
prob_all = 0
for sol in allsols(n):
    prob = 1
    for i in range(1, n+1):
        if i in sol:
            prob *= 1 / (1 + i)
        else:
            prob *= 1 - 1 / (1 + i)
    prob_all += prob

print ceil(1-prob_all)/prob_all), prob_all